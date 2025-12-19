import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('house_price_model.pkl')

st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict the estimated price")

# Numeric inputs
area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, value=3000)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
stories = st.number_input("Stories", min_value=1, max_value=5, value=2)
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)

# Categorical inputs
mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["Semi-furnished", "Unfurnished", "Furnished"]
)

# --- FEATURE ORDER (must match training exactly) ---
feature_order = [
    'area',
    'bedrooms',
    'bathrooms',
    'stories',
    'mainroad',
    'guestroom',
    'basement',
    'hotwaterheating',
    'airconditioning',
    'parking',
    'prefarea',
    'furnishingstatus_semi-furnished',
    'furnishingstatus_unfurnished'
]


# Convert inputs to model format
input_data = {
    'area': area,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'stories': stories,
    'mainroad': 1 if mainroad == "Yes" else 0,
    'guestroom': 1 if guestroom == "Yes" else 0,
    'basement': 1 if basement == "Yes" else 0,
    'hotwaterheating': 1 if hotwaterheating == "Yes" else 0,
    'airconditioning': 1 if airconditioning == "Yes" else 0,
    'parking': parking,
    'prefarea': 1 if prefarea == "Yes" else 0,
    'furnishingstatus_semi-furnished': 1 if furnishingstatus == "Semi-furnished" else 0,
    'furnishingstatus_unfurnished': 1 if furnishingstatus == "Unfurnished" else 0
}


input_df = pd.DataFrame([input_data])[feature_order]


# Prediction
if st.button("Predict House Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"🏷️ Estimated House Price: ₹ {prediction:,.2f}")
