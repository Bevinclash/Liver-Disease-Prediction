
import streamlit as st
import pandas as pd
import joblib

# Load trained ML pipeline
model = joblib.load("liver_disease_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Liver Disease Prediction",
    page_icon="🩺",
    layout="centered"
)

# Application title
st.title("🩺 Liver Disease Prediction")
st.write(
    "An educational machine learning demonstration "
    "using a Random Forest model."
)

st.warning(
    "This tool is for educational purposes only. "
    "It is not a medical diagnostic tool."
)

st.divider()

# Patient information
st.subheader("Enter Patient Details")

age = st.number_input(
    "Age (years)", min_value=1, max_value=120, value=35
)

gender = st.selectbox(
    "Gender", ["Male", "Female"]
)

# Liver test parameters
st.subheader("Liver Function Test Parameters")

col1, col2 = st.columns(2)

with col1:
    total_bilirubin = st.number_input(
        "Total Bilirubin", min_value=0.0, value=0.8
    )

    direct_bilirubin = st.number_input(
        "Direct Bilirubin", min_value=0.0, value=0.2
    )

    alkaline_phosphotase = st.number_input(
        "Alkaline Phosphotase", min_value=0.0, value=200.0
    )

    alamine_aminotransferase = st.number_input(
        "Alamine Aminotransferase", min_value=0.0, value=25.0
    )

    aspartate_aminotransferase = st.number_input(
        "Aspartate Aminotransferase", min_value=0.0, value=25.0
    )

with col2:
    total_proteins = st.number_input(
        "Total Proteins", min_value=0.0, value=6.5
    )

    albumin = st.number_input(
        "Albumin", min_value=0.0, value=3.5
    )

    albumin_globulin_ratio = st.number_input(
        "Albumin and Globulin Ratio",
        min_value=0.0,
        value=1.0
    )

st.divider()

# Prediction button
if st.button("Predict", type="primary"):

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Total_Bilirubin": total_bilirubin,
        "Direct_Bilirubin": direct_bilirubin,
        "Alkaline_Phosphotase": alkaline_phosphotase,
        "Alamine_Aminotransferase": alamine_aminotransferase,
        "Aspartate_Aminotransferase": aspartate_aminotransferase,
        "Total_Proteins": total_proteins,
        "Albumin": albumin,
        "Albumin_and_Globulin_Ratio": albumin_globulin_ratio
    }])

    # Generate prediction
import sklearn
import sys

st.write("Python version:", sys.version)
st.write("Scikit-learn version:", sklearn.__version__)
st.write("Input shape:", input_data.shape)
st.write("Input columns:", list(input_data.columns))

st.write("Model type:", type(model))
st.write("Pipeline steps:", model.named_steps.keys())
prediction = model.predict(input_data)[0]

    # Generate probability
    probabilities = model.predict_proba(input_data)[0]

    disease_probability = probabilities[1] * 100

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Model prediction: Liver Disease class (1)")
    else:
        st.success("Model prediction: No Liver Disease class (0)")

    st.metric(
        "Model-estimated probability of Liver Disease",
        f"{disease_probability:.2f}%"
    )

    st.caption(
        "This probability is a model output, not an individual's "
        "clinically established risk."
    )
    
