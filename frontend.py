import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"

# Page configuration
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🏥",
    layout="centered"
)

# Title
st.title("🏥 Insurance Premium Category Predictor")
st.markdown("Enter your details below to predict your insurance premium category.")

# Input fields
age = st.number_input(
    "Age",
    min_value=1,
    max_value=119,
    value=30
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    value=65.0
)

height = st.number_input(
    "Height (m)",
    min_value=0.5,
    max_value=2.5,
    value=1.70
)

income_lpa = st.number_input(
    "Annual Income (LPA)",
    min_value=0.1,
    value=10.0
)

smoker = st.selectbox(
    "Are you a smoker?",
    options=[True, False]
)

city = st.text_input(
    "City",
    value="Mumbai"
)

occupation = st.selectbox(
    "Occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job"
    ]
)

# Predict button
if st.button("Predict Premium Category"):

    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:

            result = response.json()

            st.success(
                f"Predicted Insurance Premium Category: {result['predicted_category']}"
            )

            # Show submitted data
            with st.expander("View Submitted Data"):
                st.json(input_data)

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Could not connect to FastAPI server.\n\n"
            "Make sure the backend is running:\n"
            "uvicorn app:app --reload"
        )

    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")