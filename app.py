import streamlit as st
import pandas as pd
import joblib

# =========================
# Load Model
# =========================
model = joblib.load("churn_model.pkl")

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.title("📊 Churn Prediction")

    st.write(
        "Machine Learning application for predicting customer churn."
    )

    st.divider()

    st.subheader("Model Information")

    st.write("**Model:** Tuned Random Forest")
    st.write("**Task:** Binary Classification")
    st.write("**ROC-AUC:** 0.840")

    st.divider()

    st.caption("Built with Python, Scikit-learn & Streamlit")

# =========================
# Main Title
# =========================
st.title("📊 Customer Churn Prediction")

st.write(
    "Enter the customer's information to estimate the probability "
    "that the customer will churn."
)

st.divider()

# =========================
# Customer Information
# =========================

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    SeniorCitizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    Partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

with col2:
    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    PhoneService = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    MultipleLines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

with col3:
    InternetService = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    Contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

# =========================
# Services
# =========================

st.subheader("🛠️ Services")

col1, col2, col3 = st.columns(3)

with col1:
    OnlineSecurity = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col2:
    DeviceProtection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    TechSupport = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

with col3:
    StreamingTV = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    StreamingMovies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

# =========================
# Payment & Charges
# =========================

st.subheader("💳 Payment & Charges")

col1, col2, col3 = st.columns(3)

with col1:
    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with col2:
    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

with col3:
    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

# =========================
# Service Count
# =========================

ServiceCount = st.number_input(
    "Service Count",
    min_value=0,
    max_value=20,
    value=5
)

st.divider()

# =========================
# Prediction Button
# =========================

predict_button = st.button(
    "🔮 Predict Customer Churn",
    use_container_width=True
)

if predict_button:

    input_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [SeniorCitizen],
        "Partner": [Partner],
        "Dependents": [Dependents],
        "tenure": [tenure],
        "PhoneService": [PhoneService],
        "MultipleLines": [MultipleLines],
        "InternetService": [InternetService],
        "OnlineSecurity": [OnlineSecurity],
        "OnlineBackup": [OnlineBackup],
        "DeviceProtection": [DeviceProtection],
        "TechSupport": [TechSupport],
        "StreamingTV": [StreamingTV],
        "StreamingMovies": [StreamingMovies],
        "Contract": [Contract],
        "PaperlessBilling": [PaperlessBilling],
        "PaymentMethod": [PaymentMethod],
        "MonthlyCharges": [MonthlyCharges],
        "TotalCharges": [TotalCharges],
        "ServiceCount": [ServiceCount]
    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    # =========================
    # Result
    # =========================

    st.subheader("📈 Prediction Result")

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        if prediction == 1:
            st.error(
                "⚠️ Customer is likely to churn."
            )
        else:
            st.success(
                "✅ Customer is unlikely to churn."
            )

    with result_col2:

        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

    st.progress(float(probability))

    st.caption(
        "The probability represents the model's estimated likelihood "
        "of customer churn."
    )