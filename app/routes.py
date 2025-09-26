from click import prompt
from app import app
from flask import render_template, jsonify, request
import requests
from . import geminiAI
import os

weather_api = os.getenv('weather_api_key', 'default')
@app.route('/')
def index():
    return render_template('index.html')

# API calls are done on the backend to keep all data secure such as user location and api key
@app.route('/weather')
def weather():
    try:
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        url = f'https://api.weatherapi.com/v1/current.json?key={weather_api}&q={lat},{lon}'
        data = requests.get(url)
        response = data.json()

        icon = response['current']['condition']
        day = response['current']['is_day']

        return jsonify({'weather': response,
                        'icon': icon,
                        'day': day,
                        'code': icon['code']
                        })


    except Exception as e:
        return jsonify({'error: ': str(e)})


# Gemini API call based on user question
# Error given if not prompt found
@app.route('/job_description', methods=['POST'])
def jobDescription():
    data = request.get_json()
    prompt = data.get('prompt', '').strip('')
    if prompt:
        output = geminiAI.call_gemini(prompt)
        return jsonify(output)
    else:
        return jsonify({'error: Empty prompt given'}), 400