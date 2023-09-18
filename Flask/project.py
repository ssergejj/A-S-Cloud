from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

app.config['UPLOAD_FOLDER'] = 'files' 

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/upload', methods=["POST"])
def upload_file():
    if "file" in request.files:
        file = request.files["file"]
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "File uploaded successfully"

    return "File not uploaded"


if __name__ == '__main__':
    app.run(debug=True)