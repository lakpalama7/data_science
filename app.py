import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="MPG Predictor", layout="centered")

st.title("🚗 Miles Per Gallon Predictor")
st.write("Enter car features to predict fuel efficiency")

# Load the model
@st.cache_resource
def load_model():
    return joblib.load("linear_model.pkl")

model = load_model()

# Create input fields for each feature
st.subheader("Car Features")

cylinders = st.slider(
    "Cylinders",
    min_value=3,
    max_value=8,
    value=4,
    step=1,
    help="Number of cylinders in the engine"
)

displacement = st.slider(
    "Displacement (cu in)",
    min_value=68.0,
    max_value=455.0,
    value=200.0,
    step=10.0,
    help="Engine displacement in cubic inches"
)

horsepower = st.slider(
    "Horsepower (hp)",
    min_value=46.0,
    max_value=230.0,
    value=100.0,
    step=5.0,
    help="Engine horsepower"
)

weight = st.slider(
    "Weight (lbs)",
    min_value=1613.0,
    max_value=5140.0,
    value=3000.0,
    step=100.0,
    help="Vehicle weight in pounds"
)

acceleration = st.slider(
    "Acceleration (0-60 mph, seconds)",
    min_value=8.0,
    max_value=24.8,
    value=15.0,
    step=0.5,
    help="Time to accelerate from 0 to 60 mph"
)

model_year = st.slider(
    "Model Year",
    min_value=70,
    max_value=82,
    value=76,
    step=1,
    help="Model year (70 = 1970, 82 = 1982)"
)

# Make prediction
if st.button("🔮 Predict MPG", type="primary"):
    features = np.array([[cylinders, displacement, horsepower, weight, acceleration, model_year]])
    prediction = model.predict(features)[0]
    
    st.success(f"### Predicted Miles Per Gallon: **{prediction:.2f} MPG**")
    
    # Display feature summary
    st.write("**Features Used:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Cylinders", cylinders)
        st.metric("Displacement", f"{displacement} cu in")
        st.metric("Horsepower", f"{horsepower} hp")
    with col2:
        st.metric("Weight", f"{weight} lbs")
        st.metric("Acceleration", f"{acceleration}s")
        st.metric("Model Year", f"19{model_year}")
