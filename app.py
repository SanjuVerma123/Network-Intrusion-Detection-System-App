import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Model & Files

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")
encoder = joblib.load("encoders.pkl")

st.set_page_config(page_title="Network Intrusion Detection", layout="wide")

st.title("🔐 Network Intrusion Detection System")
st.write("Detect whether network traffic is Normal or Attack")


# User Input Form

st.sidebar.header("Enter Network Features")

input_data = {}

for col in columns:
    # Handle categorical columns
    if col in ["protocol_type", "service", "flag"]:
        val = st.sidebar.text_input(f"{col} (e.g. tcp, http, SF)", "")
        input_data[col] = val
    else:
        val = st.sidebar.number_input(f"{col}", value=0.0)
        input_data[col] = val

# Convert to DataFrame
input_df = pd.DataFrame([input_data])


# Preprocessing (IMPORTANT)

try:
    for col in input_df.select_dtypes(include="object").columns:
        input_df[col] = encoder.fit_transform(input_df[col].astype(str))
except:
    st.warning("⚠️ Encoding issue: Please enter valid categorical values")

# Ensure column order
input_df = input_df.reindex(columns=columns, fill_value=0)


# Prediction

if st.button("Predict"):
    try:
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0]

        if prediction == 0:
            st.success(f"💚😊 Normal Traffic (Confidence: {max(prob)*100:.2f}%)")
        else:
            st.error(f"🚨 Attack Detected! (Confidence: {max(prob)*100:.2f}%)")

    except Exception as e:
        st.error(f"Error: {e}")


# Footer

st.write("---")
st.write("Built with Streamlit | XGBoost Model")

