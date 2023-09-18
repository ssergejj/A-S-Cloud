import os
import zipfile
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def receive_data():
    data_type = request.form['data_type']

    if data_type == 'D':
        # Receive the zip archive containing the folder
        folder_zip = request.files['file']
        folder_name = folder_zip.filename

        # Ensure a unique filename
        base_directory = "multivitamin"  # Replace with your desired directory
        folder_path = os.path.join(base_directory, folder_name)
        while os.path.exists(folder_path):
            folder_name, ext = os.path.splitext(folder_name)
            folder_name += "_copy"
            folder_path = os.path.join(base_directory, folder_name)

        folder_zip.save(folder_path)

        # Extract the zip archive to the specified directory
        with zipfile.ZipFile(folder_path, 'r') as zipf:
            zipf.extractall(base_directory)

        os.remove(folder_path)
        return jsonify({"message": f"Folder '{folder_name}' received and saved successfully."})

    elif data_type == 'F':
        # Receive a single file
        file = request.files['file']
        file_name = file.filename

        # Ensure a unique filename
        base_directory = "multivitamin"  # Replace with your desired directory
        file_path = os.path.join(base_directory, file_name)
        while os.path.exists(file_path):
            file_name, ext = os.path.splitext(file_name)
            file_name += "_copy"
            file_path = os.path.join(base_directory, file_name)

        file.save(file_path)
        return jsonify({"message": f"File '{file_name}' received and saved successfully."})

    else:
        return jsonify({"error": "Invalid data type received."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)