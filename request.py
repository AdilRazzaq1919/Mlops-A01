import requests

# Define the URL of the Flask server
url = 'http://127.0.0.1:5000/predict'

# Create the JSON payload
data = {
    'number_courses': 5,
    'time_study': 3
}

response = requests.post(url, json=data)
print(response.text)
