# 🏙️ Real Estate Analytics Web App

An interactive ML-powered web application to explore and analyze real estate properties in major Indian metro cities.  
Users can visualize pricing trends, explore properties by sector, and get personalized apartment recommendations.

🚀 **Live Demo**: [http://13.201.89.129:8501/](http://13.201.89.129:8501/)

---

## 📌 Features

- 🔍 **Property Recommendation Engine**  
  Recommends similar apartments using cosine similarity based on features like location, size, furnishing, and amenities.

- 📊 **Interactive Visualizations**  
  Sector-wise BHK distributions, price per sqft graphs, average apartment prices, and more.

- 🗺️ **Location-Based Apartment Finder**  
  Users can find apartments within a specific distance from a target location using geospatial filtering.

- 🧠 **Price Prediction Model**  
  Predicts the estimated price of an apartment using a Random Forest Regressor trained on real estate data.

- 🏢 **Multi-City Support**  
  Designed to work across Indian metro cities (Gurgaon, Delhi NCR, and more coming soon).

---

## 🛠️ Tech Stack

| Component    | Technology               |
|--------------|---------------------------|
| Frontend     | Streamlit                 |
| Backend      | Python, Pandas, NumPy     |
| ML Model     | Scikit-learn, Pickle      |
| Visuals      | Plotly, Matplotlib        |
| Geospatial   | Geopy, Haversine Formula  |
| Deployment   | AWS EC2 (Ubuntu Server)   |
| Data Storage | CSV Files (cleaned data)  |

---

## 💻 Getting Started

To run this project locally:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/real-estate-analytics.git
cd real-estate-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the app
streamlit run app.py

