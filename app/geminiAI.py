import os
import google.generativeai as genai
import redis
from .rtc import RTCLimit

# Uncomment the lines below if you run into an issue where you gemini is unable to automatically detect the API key.
# api_key = os.environ.get('GEMINI_API_KEY')
# genai.configure(api_key=api_key)


def call_gemini(prompt):
    # You can use any model to check the prompt token count as it does not use any tokens itself
    input_token = first_model.count_tokens(prompt).total_tokens

    # Uses the flash model if there is any tokens left
    if flash.generate(input_token):
        response = first_model.generate_content(prompt)
        # Increment the response to Redis database. Gemini automatically does token count
        flash.response_count(response.usage_metadata.candidates_token_count)
        return response.text
    # Otherwise use lite model
    elif lite.generate(input_token):
        response = second_model.generate_content(prompt)
        # Response incremented for proper tracking
        lite.response_count(response.usage_metadata.candidates_token_count)
        return response.text
    # If not tokens are left, return the error
    else:
        return "Token Count Exceeded"


def read_file(file_name):
    with open(f'app/static/text/{file_name}') as f:
        text = f.read()
        return text

# Change the host and port to your redis database.
flash = RTCLimit(host='localhost', port=6379, db=0, limit=900000)
lite = RTCLimit(host='localhost', port=6379, db=1, limit=900000)

# When adding more models, remember to also attach a RTCLimit class to them to keep track of the model's token usage.
# Input restriction by simply editing the systemInstructions.txt file.
first_model = genai.GenerativeModel('gemini-2.0-flash', system_instruction= read_file('systemInstructions.txt'))
second_model = genai.GenerativeModel('gemini-2.0-flash-lite', system_instruction= read_file('systemInstructions.txt'))


