# 🌦️ Weather Prediction Using Machine Learning

## 📌 Project Overview

This project predicts **temperature** based on various **weather parameters** such as humidity, dew point, wind speed, precipitation, and time features like hour, day, and month. The application is built using a **Random Forest Regression** model and deployed via **Streamlit**.

Dehradun, a city in the foothills of the Himalayas, was chosen as the region of focus due to its rapidly changing and unpredictable weather patterns.

---

## 👨‍💻 Team Member

| Name            | SAP ID    | Batch                        |
| --------------- | --------- | ---------------------------- |
| **Rudra Gupta** | 500120437 | B.Tech CSE - Batch 4 (AI/ML) |

---

## 🎯 Objectives

- To collect and preprocess real-time weather data.
- To build a predictive model to estimate **temperature**.
- To deploy the model using **Streamlit** for user-friendly access.

---

## ⚙️ Technologies Used

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **Matplotlib**, **Seaborn**
- **Plotly**
- **Streamlit**
- **Joblib** (for model persistence)

---

## 📊 Dataset and Preprocessing

- Collected data from **Dehradun** region.
- Cleaned and processed features: `dew_point`, `humidity`, `wind_speed`, `precipitation_cm`, `hour`, `day`, `month`.
- Target variable: `temperature`
- Feature scaling using `StandardScaler`.

---

## 🧠 Model Training

- Used **Random Forest Regressor**.
- Evaluation Metrics on Test Data:
  - ✅ **Mean Absolute Error (MAE):** `1.49°C`
  - ✅ **Mean Squared Error (MSE):** `3.12`
  - ✅ **R² Score:** `0.94`

---

## 🌐 Web App Features

- Input weather data (dew point, humidity, etc.).
- Choose date and time for prediction.
- Predict temperature instantly.
- User-friendly UI with CSS styling.
- Visualizations using **Plotly** and **Matplotlib**.

---

## 🚀 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/BlackJack-14/TempPrediction.git
   cd TempPrediction
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the `model.pkl` and `scaler.pkl` in the project directory.

4. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## 📈 Visualizations Included

- Temperature vs Humidity
- Temperature vs Wind Speed
- Boxplot by Month
- Hourly Temperature Trends
- Feature Distributions
- Correlation Heatmap
- Pairplots of Weather Features

---

## 🔮 Future Improvements

- Integrate advanced models like **XGBoost**, **Neural Networks**.
- Add extreme weather event predictions.
- Extend for real-time weather forecasting and alert system.
- Create a mobile app interface.

---

> Made with ❤️ by Rudra Gupta
