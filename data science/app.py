import streamlit as st
import joblib
import os
import numpy as np


@st.cache_resource
def load_model(path="dt_classifier.pkl"):
	if not os.path.exists(path):
		st.error(f"Model file not found: {path}")
		return None
	return joblib.load(path)


def main():
	st.title("Fuel Type Predictor")

	st.write("Enter car features to predict fuel type using the trained decision tree classifier.")

	engine = st.number_input("Engine (cc)", min_value=0.0, value=1200.0, step=50.0)
	mileage = st.number_input("Mileage (kmpl)", min_value=0.0, value=18.0, step=0.5)
	power = st.number_input("Power (bhp)", min_value=0.0, value=82.0, step=1.0)

	model = load_model()

	if model is None:
		return

	if st.button("Predict"):
		X = np.array([[engine, mileage, power]])
		try:
			pred = model.predict(X)
			print("fuel type: ", pred)
		except Exception as e:
			st.error(f"Prediction failed: {e}")
			return

		st.success(f"Predicted fuel type: {pred[0]}")


if __name__ == "__main__":
	main()

