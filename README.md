# Credit-Card-Fraud-Detection
This repository implements a credit fraud detection system using ML models. It includes data preprocessing, feature selection, model training, and Streamlit deployment for an interactive UI.

## Overview
This project aims to detect fraudulent transactions in credit card data using machine learning techniques. It includes data preprocessing, feature selection via a genetic algorithm, and model training with Logistic Regression, Decision Tree Classifier, and Random Forest Classifier. The best-performing model is selected based on metrics like accuracy, precision, recall, and F1 score.

## Detailed Steps

### Data Collection and Exploration:
- Load and explore the dataset to understand its structure and distribution.
- Visualize the data to identify patterns and anomalies.

### Data Preprocessing:
- Handle missing values and imbalanced classes.
- Standardize the features to ensure consistent scaling.

### Feature Selection using Genetic Algorithm:
- Implement a genetic algorithm to select the most relevant features for the model.
- This step enhances the model's performance by reducing dimensionality and focusing on the most significant features.

### Model Training and Evaluation:
- Train multiple machine learning models including Logistic Regression, Decision Tree Classifier, and Random Forest Classifier.
- Evaluate the models using metrics such as accuracy, precision, recall, and F1 score to select the best-performing model.

### Deployment using Streamlit:
- Deploy the trained model using Streamlit to create an interactive web application.
- The web app allows users to input transaction data and receive predictions on whether the transaction is fraudulent or legitimate.

## Dataset
The dataset used for this project is the Credit Card Fraud Detection Dataset from Kaggle. It contains transactions made by European cardholders in September 2013, with 492 fraudulent transactions out of 284,807 transactions.

## File Structure
- `fraud_detection.ipynb`: Jupyter notebook for data preprocessing, feature selection, and model training.
- `app.py`: Streamlit app for deploying the fraud detection system.

## Models Utilized
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

