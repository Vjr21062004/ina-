import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title("Forest Fire Prediction")

# Input fields
st.sidebar.header("Input Features")
X = st.sidebar.number_input("X-axis spatial coordinate", min_value=1, max_value=9, value=5)
Y = st.sidebar.number_input("Y-axis spatial coordinate", min_value=2, max_value=9, value=5)
month = st.sidebar.number_input("Month (1-12)", min_value=1, max_value=12, value=6)
day = st.sidebar.number_input("Day (1-7)", min_value=1, max_value=7, value=3)
FFMC = st.sidebar.number_input("FFMC", min_value=0.0, max_value=100.0, value=90.0)
DMC = st.sidebar.number_input("DMC", min_value=0.0, max_value=300.0, value=100.0)
DC = st.sidebar.number_input("DC", min_value=0.0, max_value=800.0, value=500.0)
ISI = st.sidebar.number_input("ISI", min_value=0.0, max_value=20.0, value=5.0)
temp = st.sidebar.number_input("Temperature (Celsius)", min_value=0.0, max_value=40.0, value=20.0)
RH = st.sidebar.number_input("Relative Humidity", min_value=0.0, max_value=100.0, value=50.0)
wind = st.sidebar.number_input("Wind Speed (km/h)", min_value=0.0, max_value=10.0, value=5.0)
rain = st.sidebar.number_input("Rain (mm)", min_value=0.0, max_value=10.0, value=0.0)

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'X': [X],
    'Y': [Y],
    'month': [month],
    'day': [day],
    'FFMC': [FFMC],
    'DMC': [DMC],
    'DC': [DC],
    'ISI': [ISI],
    'temp': [temp],
    'RH': [RH],
    'wind': [wind],
    'rain': [rain]
})

# Predict
if st.sidebar.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Burned Area: {prediction[0]:.2f} hectares")