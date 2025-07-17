import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Set Streamlit config
st.set_page_config(page_title="🏠 Real Estate Price Predictor", page_icon="📊", layout="wide")

# Title and Description
st.markdown("<h1 style='font-family: Poppins; font-size: 40px;'>🏠 Real Estate Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Roboto; font-size: 18px;'>Enter property details to estimate its price range accurately using our trained ML model.</p>", unsafe_allow_html=True)
st.markdown("---")

# Load model and data
with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

# --- Input Layout ---
with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        property_type = st.selectbox('🏘️ Property Type', ['flat', 'house'])
        bedrooms = float(st.selectbox('🛏️ Bedrooms', sorted(df['bedRoom'].unique().tolist())))
        balcony = st.selectbox('🌅 Balconies', sorted(df['balcony'].unique().tolist()))
        property_age = st.selectbox('📅 Property Age', sorted(df['agePossession'].unique().tolist()))

    with col2:
        sector = st.selectbox('📍 Sector', sorted(df['sector'].unique().tolist()))
        bathroom = float(st.selectbox('🚿 Bathrooms', sorted(df['bathroom'].unique().tolist())))
        furnishing_type = st.selectbox('🛋️ Furnishing', sorted(df['furnishing_type'].unique().tolist()))
        luxury_category = st.selectbox('💎 Luxury Category', sorted(df['luxury_category'].unique().tolist()))

    with col3:
        built_up_area = float(st.number_input('📐 Built Up Area (sqft)', step=10))
        servant_room = float(st.selectbox('🧹 Servant Room', [0.0, 1.0]))
        store_room = float(st.selectbox('📦 Store Room', [0.0, 1.0]))
        floor_category = st.selectbox('🏢 Floor Category', sorted(df['floor_category'].unique().tolist()))

    submitted = st.form_submit_button("🔮 Predict")

# --- Prediction Logic ---
if submitted:
    with st.spinner('Predicting...'):

        # Prepare dataframe
        data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room,
                 store_room, furnishing_type, luxury_category, floor_category]]
        columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
                   'agePossession', 'built_up_area', 'servant room', 'store room',
                   'furnishing_type', 'luxury_category', 'floor_category']
        one_df = pd.DataFrame(data, columns=columns)


        # Predict log price -> actual
        base_price = np.expm1(pipeline.predict(one_df))[0]
        low, high = base_price * 0.78, base_price * 1.22

        st.success(f"💰 Estimated Price Range: ₹ {round(low,2)} Cr - ₹ {round(high,2)} Cr")
        st.markdown("📌 *Note: This is an approximate range based on available market data and trends.*")


# ---------------- Footer ---------------- #
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Real Estate Insights India 🇮🇳</p>",
    unsafe_allow_html=True)
