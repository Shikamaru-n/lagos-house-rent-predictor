# 🏠 Lagos House Rent Predictor

A machine learning web application that predicts annual house rent prices in Lagos, Nigeria based on property characteristics and location.

## Features

- Predict annual rent prices for properties in Lagos
- Select from 9 different property types
- Choose from 16 major Lagos locations
- Support for properties with 0-10 bedrooms
- User-friendly Streamlit interface

## Property Types Supported

- Flat
- Duplex
- Bungalow
- Mini Flat
- Office Space
- Shop
- House
- Commercial Property
- Self Contain

## Locations Covered

Ajah, Apapa, Festac, Gbagada, Ikeja, Ikorodu, Ikoyi, Ilupeju, Isolo, Lekki, Maryland, Oshodi, Surulere, Victoria Island, Yaba, and Other areas.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Shikamaru-n/lagos-house-rent-predictor.git
cd lagos-house-price-prediction
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Required Files

Make sure you have these files in your project directory:
- `lagos_app.py` - Main application file
- `Lagos_house_price_model.pkl` - Trained machine learning model
- `feature_columns.pkl` - Feature column names for the model

## Usage

Run the Streamlit app:
```bash
streamlit run lagos_app.py
```

The app will open in your default web browser. Simply:
1. Select the number of bedrooms
2. Choose the property type
3. Select the location
4. Click "Predict Price" to get the estimated annual rent

## Requirements

- Python 3.7+
- streamlit
- numpy
- pandas
- scikit-learn
- joblib

## Model Information

The prediction model uses a machine learning algorithm trained on Lagos rental property data. It considers:
- Number of bedrooms
- Property type (one-hot encoded)
- Location/Area (one-hot encoded)

## Output

The app displays the estimated annual rent price in Nigerian Naira (₦).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Malachy Ugwu
