from flask import Flask, render_template, request, redirect, url_for, make_response, send_file, abort
from werkzeug.utils import secure_filename
import os
import json
import shutil
import zipfile
import hashlib

UPLOAD_FOLDER = r'Uploads'
user_data = {}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'b4f6b8316618881be25230831974a68f'

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_cookie' in request.cookies:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('register'))
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    # Login logic (checking user_data, for demonstration purposes)
    username = request.form['username']
    password = request.form['password']

    with open('data.json', 'r') as json_file:
        user_data = json.load(json_file)

    
    # Try to find the user based on the hashed username
    user_entry = None
    for user in user_data['users']:
        set_username = username + str(user['userID'])
        encoded_set_username = set_username.encode()
        hashed_try_username = hashlib.sha3_224(encoded_set_username).hexdigest()

        if user["username"] == hashed_try_username:
            user_entry = user
            break

    if user_entry is None:
        return "Username not found."

    set_password = password + str(user_entry['userID'])
    encoded_set_password = set_password.encode()
    hashed_set_password = hashlib.sha3_224(encoded_set_password).hexdigest()

    
    if user_entry["hashed_password"] == hashed_set_password:
        resp = make_response(redirect(url_for('menu')))
        resp.set_cookie('user_cookie', username, httponly=True)
        return resp
    else:
        return "Invalid password."
    

@app.route('/registration', methods=['POST'])
def submit_data():
    data = {}
    # Get data from the form
    data['username'] = request.form['username']
    data['password'] = request.form['password']

    # Save the data to a JSON file
    with open('data.json') as json_file:
        user_data = json.load(json_file)

    userID = user_data['currentUserID']

    set_password = data['password'] + str(userID)
    set_username = data['username'] + str(userID)

    # Encode the concatenated string
    encoded_set_password = set_password.encode()
    encoded_set_username = set_username.encode()

    # Hash the encoded string
    hashed_set_password = hashlib.sha3_224(encoded_set_password).hexdigest()
    hashed_set_username = hashlib.sha3_224(encoded_set_username).hexdigest()

    new_user = {
        "userID": userID,
        "username": hashed_set_username,
        "hashed_password": hashed_set_password
    }

    
    user_data['users'].append(new_user)

    # Increment the currentUserID for the next user
    user_data['currentUserID'] += 1
    
    with open('data.json', 'w') as json_file:
        json.dump(user_data, json_file)
    
    resp = make_response(redirect(url_for('menu')))
    resp.set_cookie('user_cookie', data['username'], httponly=True)
    return resp

@app.route("/menu", methods=['GET', 'POST']) 
def menu():
    return render_template('menu.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route("/upload_file", methods = ["POST"])
def upload_file():
    if "file" in request.files:
        file = request.files["file"]
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('menu'))
    return "File not uploaded"

@app.route("/download")
def file_browser():
    current_directory = 'Uploads'
    items = list_files_and_dirs(current_directory)

    return render_template('download.html', current_directory=current_directory, items=items)
    
def list_files_and_dirs(directory):
    files_and_dirs = os.listdir(directory)
    items = []
    for item in files_and_dirs:
        item_path = os.path.join(directory, item)
        is_directory = os.path.isdir(item_path)
        items.append((item, item_path, is_directory))
    return items

def get_full_path(subdirectory):
    return os.path.abspath(os.path.join(os.getcwd(), subdirectory))

@app.route('/browse/<path:subdirectory>')
def browse_directory(subdirectory):
    current_directory = get_full_path(subdirectory)
    items = list_files_and_dirs(current_directory)

    return render_template('download.html', current_directory=current_directory, items=items)

@app.route('/view/<path:file_path>')
def view_file(file_path):
    try:
        return send_file(file_path)
    except Exception:
        abort(404)

@app.route('/download/<path:file_path>')
def download_file(file_path):
    try:
        return send_file(file_path, as_attachment=True)
    except Exception:
        abort(404)

@app.route('/download_folder', methods=['POST'])
def download_folder():
    folder_path = request.form.get('folder_path')
    if folder_path:
        folder_path = get_full_path(folder_path)
        zip_filename = os.path.basename(folder_path) + '.zip'
        zip_path = os.path.join(os.getcwd(), zip_filename)

        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)

            response = make_response(send_file(zip_path, as_attachment=True, download_name=zip_filename))
            response.headers['Content-Disposition'] = f'attachment; filename="{zip_filename}"'

            return response
        except Exception:
            abort(404)
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')
