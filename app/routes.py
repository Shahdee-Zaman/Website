from click import prompt
from app import app
from flask import render_template, jsonify, request
from . import geminiAI
import os

api_key = os.getenv('weather_api_key', 'default')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather-api')
def weatherApi():
    return jsonify(api_key)

@app.route('/job_description', methods=['POST'])
def jobDescription():
    data = request.get_json()
    prompt = data.get('prompt', '').strip('')
    if prompt:
        output = geminiAI.call_gemini(prompt)
        return jsonify(output)
    else:
        return jsonify({'error: Empty prompt given'}), 400