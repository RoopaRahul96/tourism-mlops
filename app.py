import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title("Tourism Package Prediction")

age = st.number_input("Age", min_value=18, max_value=80, value=30)
income = st.number_input("Monthly Income", value=30000)
trips = st.number_input("Number of Trips", value=2)

if st.button("Predict"):

    # Create empty input with all required columns
    input_data = pd.DataFrame([[0]*len(columns)], columns=columns)

    # Fill only known features
    if "Age" in input_data.columns:
        input_data["Age"] = age
    if "MonthlyIncome" in input_data.columns:
        input_data["MonthlyIncome"] = income
    if "NumberOfTrips" in input_data.columns:
        input_data["NumberOfTrips"] = trips

    pred = model.predict(input_data)

    if pred[0] == 1:
        st.success("Customer will purchase")
    else:
        st.error("Customer will NOT purchase")
