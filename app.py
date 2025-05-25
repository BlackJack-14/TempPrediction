import streamlit as st
import joblib
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# --- Load model and scaler ---
try:
    model = joblib.load('./model.pkl')
    scaler = joblib.load('./scaler.pkl')
except FileNotFoundError:
    st.error("Error: Model or Scaler file not found. Please ensure they are in the correct location.")

# --- Page settings ---
st.set_page_config(page_title="Temperature Predictor", page_icon="🌡️", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        /* General Styling */
        body {
            background-color: #f4f4f9;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            color: #333;
            margin: 0;
            padding: 0;
        }

        .custom-header {
            text-align: center;
            color: #fff;
            font-size: 36px;
            font-weight: bold;
        }

        .subheader {
            color: #fff;
            font-size: 18px;
        }

        /* Main Container Styling */
        .main-container {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
            margin-top: 25px;
        }

        .form-section {
            margin-bottom: 20px;
        }

        /* Input Styling */
        .stNumberInput, .stTextInput, .stSelectbox, .stSlider {
            font-size: 16px;
            padding: 10px;
        }

        /* Button Styling */
        .stButton button {
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            padding: 12px 25px;
            border-radius: 5px;
            border: none;
            transition: background-color 0.3s ease;
        }

        .stButton button:hover {
            background-color: #0056b3;
        }

        /* Footer Styling */
        .footer {
            text-align: center;
            font-size: 14px;
            color: #7f8c8d;
            margin-top: 50px;
        }

        /* Chart Styling */
        .plotly-chart {
            background-color: #ffffff;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
    <div class='custom-header'>
        Temperature Prediction
    </div>
    <div class="subheader">
        Instantly predict the temperature based on weather inputs.
    </div>
""", unsafe_allow_html=True)

# --- Form Section ---
with st.form("prediction_form", clear_on_submit=False):
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.subheader("Weather Details")

    col1, col2 = st.columns(2)
    with col1:
        dew_point = st.number_input("Dew Point (°C)", min_value=0.0, max_value=50.0, step=0.1)
        wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=200.0, step=0.1)
    with col2:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
        precipitation_cm = st.number_input("Precipitation (cm)", min_value=0.0, max_value=500.0, step=0.1)

    st.markdown("<hr />", unsafe_allow_html=True)
    st.subheader("Date & Time")

    now = datetime.now()
    col3, col4, col5 = st.columns(3)
    with col3:
        hour = st.number_input("Hour (0–23)", min_value=0, max_value=23, value=now.hour)
    with col4:
        day = st.number_input("Day (1–31)", min_value=1, max_value=31, value=now.day)
    with col5:
        month = st.number_input("Month (1–12)", min_value=1, max_value=12, value=now.month)

    st.markdown("<br>", unsafe_allow_html=True)
    predict_button = st.form_submit_button("Predict Temperature")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Prediction Section ---
if predict_button:
    with st.spinner('Predicting temperature...'):
        input_data = np.array([[dew_point, humidity, wind_speed, precipitation_cm, hour, day, month]])
        input_data_scaled = scaler.transform(input_data)
        predicted_temp = model.predict(input_data_scaled)[0] + 2  # +2 for manual correction

        # Simulate a delay (optional, for realism)
        import time
        time.sleep(2)

    st.success(f"Predicted Temperature: **{predicted_temp:.2f} °C**")


