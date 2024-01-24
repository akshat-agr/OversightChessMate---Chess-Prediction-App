# OversightChessMate---Chess-Prediction-App
Overview:
OversightChessMate is a web application that predicts the likely outcome of a chess game based on the user's and opponent's ratings, as well as differences in accuracy, mistakes, and blunders. The application uses a logistic regression model trained on a dataset of chess game outcomes.

## Project Structure

- `app`: This folder contains the main Flask application code.
- `templates`: Holds the HTML templates used by Flask to render web pages.
- `static`: This folder is used to store static files such as stylesheets and images.
-  `model.py`: Python script defining the machine learning model.
- `model.pkl`: Serialized version of the trained model (you can customize the extension based on your serialization method).
- `preprocess.py`: Python script for data preprocessing.

Dependencies:
Flask
NumPy
Pandas
Pickle
Scikit-learn

Notebook Link : https://colab.research.google.com/drive/1ID417lXQqZON3lPvWWihSTBlL3IGAnwq?usp=sharing
