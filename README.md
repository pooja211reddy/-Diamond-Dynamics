💎 Diamond Dynamics
Price Prediction & Market Segmentation using ML
📌 Overview

Diamond Dynamics is a machine learning project that predicts diamond prices and segments diamonds into meaningful market categories using clustering techniques.

This project combines:

🔮 Regression (XGBoost) → Price prediction
📊 Clustering (K-Means) → Market segmentation
🌐 Streamlit UI → Interactive dashboard
🚀 Features
💰 Predict diamond price (USD & INR)
📊 Segment diamonds into market categories
📈 Interactive visualizations:
Price distribution
Cluster scatter plots (Carat vs Price)
Cluster distribution bar chart
🎯 User input-based real-time prediction
🎨 Clean and modern UI using Streamlit
🧠 Machine Learning Models
1. Price Prediction
Model: XGBoost Regressor
Target: price (log-transformed)
Evaluation:
MAPE: ~6.79%
Accuracy: ~93.2%
2. Market Segmentation
Model: K-Means Clustering (k=5)
Features used:
carat, cut, color, clarity, depth, table, volume
Output clusters:
Very Cheap Tiny Diamonds
Affordable Small Diamonds
Mid-range Diamonds
High Value Diamonds
Premium Luxury Diamonds
📊 Visualizations
🔹 Carat vs Price Clustering
Shows distribution of diamonds across clusters
🔹 Price Distribution
Histogram with user’s predicted price highlighted
🔹 Cluster Distribution
Number of diamonds per segment
🖥️ Streamlit App
UI Components:
Input fields:
Carat, Cut, Color, Clarity, Dimensions
Buttons:
Predict Price
Predict Market Segment
Outputs:
Price (USD + INR)
Cluster + Segment
Graphs:
Scatter plot
Histogram
Bar chart
⚙️ Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn
XGBoost
Plotly & Matplotlib
Streamlit
📂 Project Structure
📁 Diamond-Dynamics
│
├── 📄 Diamond_app.py        # Streamlit app
├── 📄 Diamond_predictor.ipynb
├── 📄 kmeans_model.pkl
├── 📄 scaler.pkl
├── 📄 xgboost_model.pkl
├── 📄 diamonds.csv
└── 📄 README.md
▶️ How to Run
pip install -r requirements.txt
streamlit run Diamond_app.py
📈 Sample Output
Predicted Price: $3,361 (~₹2.78L)
Segment: Mid-range Diamonds / Premium (based on input)
⚠️ Challenges Faced
Handling categorical encoding consistency
Feature mismatch between training & prediction
Scaling issues with StandardScaler
Cluster interpretation (unsupervised learning)
💡 Future Improvements
🔥 Use PCA for better clustering visualization
📊 Add SHAP for model explainability
☁️ Deploy on Streamlit Cloud / AWS
🤖 Improve clustering with DBSCAN or GMM
📱 Make mobile-friendly UI
🙌 Author

Pooja Nandini
Capstone Project – Diamond Dynamics
