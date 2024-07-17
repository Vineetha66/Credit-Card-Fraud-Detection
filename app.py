import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
with open(r'C:/Users/Vineetha Juttiga/Credit Card Fraud Detection/Model/RF_Model.pkl' , 'rb') as model_file:
    model = pickle.load(model_file)

def predict_fraud(distance_from_home, distance_from_last_transaction, 
                  ratio_to_median_purchase_price, repeat_retailer,
                  used_chip, used_pin_number, online_order):
    # Create a NumPy array with the input features
    input_data = np.array([[distance_from_home, distance_from_last_transaction,
                            ratio_to_median_purchase_price, repeat_retailer,
                            used_chip, used_pin_number, online_order]])

    # Make a prediction
    prediction = model.predict(input_data)

    return prediction[0]

# Streamlit app layout
st.title('Credit Card Fraud Detection')

# Input fields
distance_from_home = st.number_input('Distance from Home', value=0.0)
distance_from_last_transaction = st.number_input('Distance from Last Transaction', value=0.0)
ratio_to_median_purchase_price = st.number_input('Ratio to Median Purchase Price', value=0.0)
repeat_retailer = st.checkbox('Repeat Retailer')
used_chip = st.checkbox('Used Chip')
used_pin_number = st.checkbox('Used PIN Number')
online_order = st.checkbox('Online Order')

# Make prediction on button click
if st.button('Predict'):
    result = predict_fraud(distance_from_home, distance_from_last_transaction, 
                           ratio_to_median_purchase_price, repeat_retailer,
                           used_chip, used_pin_number, online_order)

    if result == 1:
        st.error("It's a Fraud Transaction")
    else:
        st.success("It's a Genuine Transaction")
