import streamlit as st
import numpy as np
import pandas as pd
import joblib 

# Load model and related data
model = joblib.load('Lagos_house_price_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

property_types = ['flat', 'duplex', 'bungalow', 'mini flat', 'office space', 'shop', 'house', 'commercial property', 'self contain']

areas = ['ajah', 'apapa', 'festac', 'gbagada', 'ikeja', 'ikorodu', 'ikoyi','ilupeju', 'isolo', 'lekki', 'maryland', 'oshodi', 'other','surulere', 'victoria island', 'yaba']

bedrooms = list(range(0, 11))

st.title("🏠 Lagos House Rent Predictor")

# User inputs
selected_bedrooms = st.selectbox("Number of Bedrooms", bedrooms)
selected_property_type = st.selectbox("Property Type", property_types)
selected_area = st.selectbox("Location (Area)", areas)

if st.button("Predict Price"):
    # Initialize zero vector
    x = np.zeros(len(feature_columns))

    # Set numerical and categorical features
    x[feature_columns.index('No_of_Bedrooms')] = selected_bedrooms
    prop_col = f'property_type_{selected_property_type.lower()}'
    area_col = f'area_{selected_area.lower()}'

    if prop_col in feature_columns:
        x[feature_columns.index(prop_col)] = 1

    if area_col in feature_columns:
        x[feature_columns.index(area_col)] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([x], columns=feature_columns)

    # Predict
    prediction = model.predict(input_df)[0]
    
    # Display result
    st.success(f"Estimated Annual Rent Price: ₦{int(prediction):,}")
