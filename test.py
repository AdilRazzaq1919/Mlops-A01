import requests
import json

# Define the input data for prediction
input_data = {
    'number_courses': 5,
    'time_study': 4
}

# URL of the Flask app endpoint for prediction
url = 'http://127.0.0.1:5000/predict'

# Send a POST request with input data to the Flask app
try:
    response = requests.post(url, json=input_data)
    if response.status_code == 200:
        result = response.json()
        print(f"Predicted Marks: {result['predicted_marks']}")
    else:
        print(f"Error occurred: {response.text}")
except Exception as e:
    print(f"Exception occurred: {str(e)}")
