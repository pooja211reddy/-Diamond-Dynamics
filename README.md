💎 Diamond Dynamics
🚀 Price Prediction & Market Segmentation using Machine Learning
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python"> <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit"> <img src="https://img.shields.io/badge/XGBoost-Model-orange"> <img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow?logo=scikitlearn"> <img src="https://img.shields.io/badge/Status-Completed-brightgreen"> </p>
🎯 Project Overview

Diamond Dynamics is an end-to-end ML application that:

🔮 Predicts diamond prices using XGBoost
📊 Segments diamonds into market categories using K-Means
🌐 Provides an interactive Streamlit dashboard
🖼️ App Preview
📊 Dashboard UI

🎥 Demo (Optional GIF)

👉 (Replace these with your real screenshots — I’ll show how below)

🚀 Features
💰 Real-time Price Prediction (USD & INR)
📊 Market Segmentation using clustering
📈 Interactive Visualizations:
Carat vs Price Scatter Plot
Price Distribution with prediction line
Cluster Distribution Bar Chart
🎯 User input-based predictions
🎨 Clean & modern UI
🧠 Machine Learning Models
🔹 Price Prediction
Model: XGBoost Regressor
Target: log(price)
Performance:
📉 MAPE: ~6.79%
🎯 Accuracy: ~93.2%
🔹 Market Segmentation
Model: K-Means (k=5)

Features Used:

carat, cut, color, clarity, depth, table, volume

Segments:

🟢 Affordable Small Diamonds
🔵 Mid-range Diamonds
🟡 High Value Diamonds
🔴 Premium Luxury Diamonds
⚪ Very Cheap Tiny Diamonds
📊 Visualizations
Plot	Description
📉 Scatter Plot	Carat vs Price with clusters
📊 Histogram	Price distribution + your prediction
📦 Bar Chart	Cluster distribution
🖥️ Streamlit App
🔹 Inputs
Carat
Cut
Color
Clarity
Dimensions
🔹 Outputs
💰 Predicted Price
📊 Cluster
🏷️ Market Segment
⚙️ Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn
XGBoost
Plotly & Matplotlib
Streamlit
📂 Project Structure
Diamond-Dynamics/
│
├── Diamond_app.py
├── Diamond_predictor.ipynb
├── kmeans_model.pkl
├── scaler.pkl
├── xgboost_model.pkl
├── diamonds.csv
└── README.md
▶️ Run Locally
pip install -r requirements.txt
streamlit run Diamond_app.py
📈 Sample Output
💰 Price: $3,361 (~₹2.78L)
🏷️ Segment: Mid-range Diamonds
⚠️ Challenges Faced
Encoding categorical variables consistently
Feature mismatch between training & inference
Scaling issues with StandardScaler
Interpreting unsupervised clusters
💡 Future Improvements
🔥 PCA for better clustering visualization
📊 SHAP for explainability
☁️ Deploy on Streamlit Cloud
🤖 Try DBSCAN / GMM
📱 Mobile UI improvements
👩‍💻 Author

Pooja Reddy
Capstone Project – Diamond Dynamics
