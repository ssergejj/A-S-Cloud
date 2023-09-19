from flask import Flask, render_template, request,flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = r'C:\Users\admin\Documents\VSC\A-S-Cloud\Flask'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('index.html', error=error)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('form.html')
    file=request.files['file']
def upload_file():
    if request.method == 'POST':
        import os
        upload.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename))

if __name__ == '__main__':
    app.run(debug=True)