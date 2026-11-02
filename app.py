
import streamlit as st
import pickle
import pandas as pd

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Student Performance Prediction")

st.write("Predict student marks")

hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.slider(
    "Attendance",
    0, 100, 75
)

if st.button("Predict Marks"):
    data = pd.DataFrame({
        "Study_Hours": [hours],
        "Attendance": [attendance]
    })

    result = model.predict(data)[0]

    st.success(f"Predicted Marks: {result:.2f}")
