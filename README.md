# Titanic Survival Prediction App

Overview The Titanic Survival Prediction App is an interactive machine learning web application built using Streamlit, designed to predict whether a passenger survived the Titanic disaster based on key passenger details. This app leverages a trained Logistic Regression model and offers a user-friendly interface to input passenger information and obtain real-time predictions.

## Key Features
Survival Prediction: Users input passenger details, and the app predicts whether the passenger survived the Titanic disaster.

Real-Time Prediction: The app utilizes a pre-trained Logistic Regression model to deliver immediate predictions.

Interactive User Interface: Built with Streamlit, the app offers an easy-to-use interface for interacting with the model.

Dynamic Data Processing: Handles both categorical and numerical inputs, including encoding and scaling.

## Input Features:
. Passenger Class (Pclass)
. Sex
. Age
. Siblings/Spouses Aboard (SibSp)
. Parents/Children Aboard (Parch)
. Fare
. Embarked Port (Embarked)

## Model:
The app uses a Logistic Regression model trained on the Titanic dataset from Kaggle, which classifies passengers as either survived or not based on the provided features.

## Technologies
. Python

. Streamlit: For creating the interactive web application.

. scikit-learn: For the machine learning model (Logistic Regression).

. pandas: For data manipulation and preprocessing.

. MinMaxScaler: For scaling features to ensure model accuracy.
. Seaborn and Ploty for visualization
