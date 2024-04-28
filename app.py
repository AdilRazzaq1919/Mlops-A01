from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

# Load the data
data = pd.read_csv('Student_Marks.csv')

# Split the data
X = data[['number_courses', 'time_study']]
y = data['Marks']
X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
model_filename = 'Student_Marks_Model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

# Load the model
with open(model_filename, 'rb') as file:
    model = pickle.load(file)


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        number_courses = data['number_courses']
        time_study = data['time_study']
        prediction = model.predict(np.array([[number_courses, time_study]]))[0]
        return jsonify({'predicted_marks': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
