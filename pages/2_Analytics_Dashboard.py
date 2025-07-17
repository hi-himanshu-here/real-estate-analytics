import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
df = pd.read_csv('data/data_viz1.csv')
feature_text = pickle.load(open('data/feature_text.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Real Estate Analytics", layout="wide")

# ---- STYLING ----
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
        }

        .metric-label, .metric-value {
            font-size: 18px !important;
        }

        .title {
            font-size: 36px;
            font-weight: 600;
            margin-bottom: 0;
        }

        .subtitle {
            font-size: 24px;
            font-weight: 500;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<div class='title'>🏡 Real Estate Analytics Dashboard</div>", unsafe_allow_html=True)
st.markdown("---")

# ---- METRICS ----
avg_price = round(float(df['price'].mean(skipna=True)), 2)
avg_area = round(float(df['built_up_area'].mean(skipna=True)), 2)
avg_price_per_sqft = round(float(df['price_per_sqft'].mean(skipna=True)), 2)

col1, col2, col3 = st.columns(3)
col1.metric("Avg Price", f"₹ {avg_price} Cr")
col2.metric("Avg Area", f"{avg_area} sqft")
col3.metric("Avg Price/Sqft", f"₹ {avg_price_per_sqft}")

# ---- SECTOR PRICE GEO MAP ----
st.markdown("<div class='subtitle'>📍 Sector Price per Sqft Map</div>", unsafe_allow_html=True)

group_df = df.groupby('sector').mean(numeric_only=True)[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                        color_continuous_scale="Viridis", zoom=10, mapbox_style="open-street-map",
                        hover_name=group_df.index, width=1100, height=600)
st.plotly_chart(fig, use_container_width=True)

# ---- WORDCLOUD OVERALL ----
st.markdown("<div class='subtitle'>🧠 Overall Features WordCloud</div>", unsafe_allow_html=True)
wc = WordCloud(width=800, height=400, background_color='black').generate(feature_text)

fig_wc = plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
st.pyplot(fig_wc)

# ---- AREA VS PRICE ----
st.markdown("<div class='subtitle'>📊 Area vs Price by Property Type</div>", unsafe_allow_html=True)
prop_type = st.selectbox('Choose Property Type:', df['property_type'].unique())

fig_area_price = px.scatter(df[df['property_type'] == prop_type],
                            x='built_up_area', y='price', color='bedRoom',
                            title=f"Area vs Price for {prop_type.title()}s")
st.plotly_chart(fig_area_price, use_container_width=True)

# ---- BHK PIE CHART ----
st.markdown("<div class='subtitle'>🥧 BHK Distribution</div>", unsafe_allow_html=True)
sector = st.selectbox('Select Sector:', ['Overall'] + sorted(df['sector'].unique()))

if sector == 'Overall':
    fig_bhk = px.pie(df, names='bedRoom', title='BHK Distribution - Overall')
else:
    fig_bhk = px.pie(df[df['sector'] == sector], names='bedRoom', title=f'BHK Distribution - {sector}')
st.plotly_chart(fig_bhk, use_container_width=True)

# ---- BHK PRICE COMPARISON ----
st.markdown("<div class='subtitle'>📦 BHK Price Comparison (Box Plot)</div>", unsafe_allow_html=True)
fig_box = px.box(df[df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK-wise Price Range')
st.plotly_chart(fig_box, use_container_width=True)

# ---- HISTPLOT BY PROPERTY TYPE ----
st.markdown("<div class='subtitle'>📈 Price Distribution by Property Type</div>", unsafe_allow_html=True)
fig_dist = plt.figure(figsize=(10, 4))
sns.histplot(df[df['property_type'] == 'flat']['price'], kde=True, label='Flat', color='skyblue')
sns.histplot(df[df['property_type'] == 'house']['price'], kde=True, label='House', color='salmon')
plt.legend()
plt.title("Price Distribution by Property Type")
st.pyplot(fig_dist)


# ---- Additional ----

# ---- FOOTER ----
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Real Estate Insights India 🇮🇳</p>",
    unsafe_allow_html=True)
