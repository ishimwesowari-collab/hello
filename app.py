import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# 1. Load your trained model
model_path = Path(__file__).parent / "25rp18587.pkl"
if not model_path.is_file():
    st.error(f"Model file not found: {model_path}")
    st.stop()

with open(model_path, "rb") as f:
    loaded_model = pickle.load(f)

# 2. App title
st.title("🌾 Crop Yield Prediction (Temperature‑only)")

# 3. Input for temperature
temperature = st.number_input(
    "Temperature (°C):",
    min_value=-10.0,
    max_value=50.0,
    step=0.1,
    value=25.0
)

# 4. Prepare input dataframe
input_df = pd.DataFrame([{"Temperature": temperature}])

# 5. Predict on button click
if st.button("Predict Yield"):
    try:
        prediction = loaded_model.predict(input_df)
        st.success(f"Predicted Crop Yield: {prediction[0]:.2f} tons per hectare")
    except Exception as e:
        st.error(f"Prediction error: {e}")
