from flask import Flask, render_template, send_file, abort, make_response, request
import os
import shutil
import zipfile

app = Flask(__name__)

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

@app.route('/')
def file_browser():
    current_directory = os.getcwd()
    items = list_files_and_dirs(current_directory)

    return render_template('index.html', current_directory=current_directory, items=items)

@app.route('/browse/<path:subdirectory>')
def browse_directory(subdirectory):
    current_directory = get_full_path(subdirectory)
    items = list_files_and_dirs(current_directory)

    return render_template('index.html', current_directory=current_directory, items=items)

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
    app.run(debug=True)
