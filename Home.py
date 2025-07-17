import streamlit as st

st.set_page_config(
    page_title="India Metro Real Estate Analytics",
    page_icon="🏙️",
    layout="wide"
)

st.title("🏙️ Welcome to the India Metro Real Estate Analytics App!")

st.markdown("""
### Unlock Real Estate Insights Across India's Top Metro Cities

This powerful and interactive analytics platform helps you explore the real estate landscape of India's major metro cities — including **Delhi NCR (Gurgaon, Noida)**, **Mumbai**, **Bangalore**, **Hyderabad**, **Chennai**, **Pune**, and more.

Whether you're a **homebuyer**, **investor**, or **real estate consultant**, this app empowers you to:

- 📊 **Visualize** property trends, sector-wise prices, and BHK-wise comparisons  
- 🏘️ **Compare apartments** within and across cities, sectors, and neighborhoods  
- 📍 **Find nearby properties** based on custom location and radius filters  
- 🌟 **Get personalized apartment recommendations** using similarity-based algorithms  
- 🤖 **Predict property prices** using machine learning models trained on real city data  

---

### 🔧 Key Features

- 🗺️ Support for **multiple metro cities**
- 📉 Interactive data visualizations (BHK, sector, price trends)
- 🤝 Apartment recommendation system
- 💬 Price prediction engine with detailed inputs
- 🔍 Search properties within radius of any location

---

### 📌 How to Use the App

1. Select a city and navigate to the desired feature using the **sidebar**
2. Use interactive tools to analyze trends or get recommendations
3. Make smarter, data-driven real estate decisions with confidence

---

### 🚀 Cities Currently Supported

- Delhi NCR (Gurgaon, Noida, Ghaziabad)  
- Mumbai  
- Bangalore  
- Pune *(coming soon)*
- Hyderabad *(coming soon)*
- Chennai *(coming soon)*
- Kolkata *(coming soon)*

---

Start exploring India's real estate market through the power of data and AI!
""")


# ---------------- Footer ---------------- #
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Real Estate Insights India 🇮🇳</p>",
    unsafe_allow_html=True)
