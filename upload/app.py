from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files' 

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/upload', methods=["POST"])
def upload_file():
    if "file" in request.files:
        file = request.files["file"]
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "File uploaded successfully"

    return "File not uploaded"

if __name__ == "__main__":
    app.run(debug=True)
