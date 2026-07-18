import joblib
import streamlit as st
import pandas as pd

st.title("MPG Prediction")

model = joblib.load("linear_model.pkl")

cylinders = st.number_input("Cylinders", min_value=1, max_value=16, value=4, step=1)
displacement = st.number_input("Displacement", min_value=50.0, max_value=500.0, value=150.0)
horsepower = st.number_input("Horsepower", min_value=10.0, max_value=500.0, value=100.0)
weight = st.number_input("Weight", min_value=500.0, max_value=7000.0, value=3000.0)
acceleration = st.number_input("Acceleration", min_value=1.0, max_value=30.0, value=15.0)
model_year = st.number_input("Model Year", min_value=60, max_value=99, value=76, step=1)

if st.button("Predict MPG"):
    data = pd.DataFrame(
        [[cylinders, displacement, horsepower, weight, acceleration, model_year]],
        columns=[
            "cylinders",
            "displacement",
            "horsepower",
            "weight",
            "acceleration",
            "model_year",
        ],
    )
    prediction = model.predict(data)
    st.write(f"Predicted MPG: {prediction[0]:.2f}")
