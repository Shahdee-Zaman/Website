from app import app
from flask import render_template, jsonify
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather-api')
def weatherApi():
    file_path = 'Your api key'
    if not os.path.isfile(file_path):
        print('File not found')
    try:
        with open(file_path, 'r') as f:
            return jsonify(f.readline())
    except FileNotFoundError:
        print('File not found!!')
