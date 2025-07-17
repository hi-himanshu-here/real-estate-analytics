import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Set the page configuration
st.set_page_config(
    page_title="Apartment Recommender",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
location_df = pickle.load(open('data/location_distance.pkl', 'rb'))
cosine_sim1 = pickle.load(open('data/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('data/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('data/cosine_sim3.pkl', 'rb'))


# ---------------- Recommendation Function ---------------- #
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()

    return pd.DataFrame({
        '🏢 Property Name': top_properties,
        '📊 Similarity Score': [round(score, 3) for score in top_scores]
    })


# ----------------- Title ------------------ #
st.markdown("<h1 style='font-family:Georgia; font-size:42px; color:#4B8BBE;'>🏙️ Smart Apartment Recommender</h1>",
            unsafe_allow_html=True)
st.markdown(
    "<p style='font-size:18px;'>Explore apartments near your preferred locations or discover similar apartments based on your choice. Powered by similarity-based recommendations using multiple features.</p>",
    unsafe_allow_html=True)
st.markdown("---")

# ---------------- Location & Radius Section ---------------- #
st.markdown("### 📍 Search Nearby Apartments")
col1, col2 = st.columns(2)

with col1:
    selected_location = st.selectbox('Choose a Location:', sorted(location_df.columns.to_list()))
with col2:
    radius = st.number_input('Enter Radius (in kms):', min_value=0.0, step=0.5)

if st.button('🔍 Find Nearby Apartments'):
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

    if result_ser.empty:
        st.warning("No apartments found within the selected radius.")
    else:
        st.success(f"Apartments within {radius} km of {selected_location}:")
        for key, value in result_ser.items():
            st.markdown(f"• **{key}** — {round(value / 1000, 2)} km")

st.markdown("---")

# ---------------- Recommendation Section ---------------- #
st.markdown("### 🤝 Recommend Similar Apartments")
selected_apartment = st.selectbox('Select an Apartment to Get Recommendations:', sorted(location_df.index.to_list()))

if st.button('✨ Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment)
    if not recommendation_df.empty:
        st.markdown("#### 🏡 Top Similar Apartments")
        st.dataframe(recommendation_df.style.set_properties(**{
            'text-align': 'left',
            'font-family': 'Arial',
            'font-size': '16px'
        }), use_container_width=True)
    else:
        st.warning("No recommendations found. Try a different apartment.")

# ---------------- Footer ---------------- #
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Real Estate Insights India 🇮🇳</p>",
    unsafe_allow_html=True)
