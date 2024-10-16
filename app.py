# app.py

from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file is an allowed type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for admin login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # You can change this to a more secure method
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials!')
            return redirect(url_for('login'))
    return render_template('login.html')

# Route for the dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(f'File {filename} uploaded successfully!')
            process_excel(file)  # Function to process the uploaded Excel file
            return redirect(url_for('dashboard'))

    # Render dashboard with the latest timestamp
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('dashboard.html', last_updated=last_updated)

def process_excel(file):
    df = pd.read_excel(file)
    # Process the data as per your requirements (filtering, chart data extraction, etc.)
    # Save or return the processed data

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
