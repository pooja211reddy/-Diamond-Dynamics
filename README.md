# 💎 Diamond Dynamics  
### 🚀 Price Prediction & Market Segmentation using Machine Learning  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/XGBoost-Model-orange">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow?logo=scikitlearn">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
</p>

---

## 🎯 Overview

Diamond Dynamics is an end-to-end machine learning application that:

- 🔮 Predicts diamond prices using **XGBoost**
- 📊 Segments diamonds into market categories using **K-Means clustering**
- 🌐 Provides an interactive **Streamlit dashboard**

---

## 🖼️ App Preview

### 📊 Dashboard UI
![App Screenshot](images/dashboard.png)

---

### 🎥 Demo
![Demo GIF](images/demo.gif)

---
### 📦 Dataset
📁 Diamonds Dataset
🔢 ~53,940 rows × 10 features
🎯 Target: price (log-transformed)
Features Used
carat, cut, color, clarity, depth, table, volume

---

### 🤖 Model Comparison
Model	MAE ↓	RMSE ↓	R² ↑
🥇 XGBoost	214.11	367.05	0.988
Random Forest	213.21	389.79	0.986
Decision Tree	272.96	514.45	0.976
KNN	296.23	537.55	0.974
ANN	323.96	549.42	0.973
❌ Linear Regression	1133.66	2281.33	0.543

---

### 🔹 Price Prediction Model
- Model: **XGBoost Regressor**
- Target: `log(price)`
- Performance:
  - 📉 MAPE: **~6.79%**
  - 🎯 Accuracy: **~93.2%**

👉 Final Model: XGBoost Regressor

---

### 🔍 Clustering (Market Segmentation)
📈 Elbow Method
<p align="center"> <img src="assets/elbow.png" width="60%"/> </p>
Optimal cluster point: K = 5
After K=5, improvement slows down
### 🏷️ Diamond Segments
Cluster	Segment
0	💎 Premium Luxury Diamonds
1	💰 High Value Diamonds
2	📊 Mid-range Diamonds
3	🟢 Affordable Small Diamonds
4	⚪ Very Cheap Tiny Diamonds

---
### ⚙️ Tech Stack
🐍 Python
📊 Pandas, NumPy
🤖 Scikit-learn
⚡ XGBoost
📈 Plotly & Matplotlib
🌐 Streamlit

---

### 📁 Project Structure
Diamond-Dynamics/
│── Diamond_app.py        # Streamlit app
│── Diamond_predictor.ipynb
│── kmeans_model.pkl
│── scaler.pkl
│── xgboost_model.pkl
│── diamonds.csv
│── requirements.txt
│── README.md
│── assets/
│   ├── dashboard.png
│   ├── elbow.png
│   └── demo.gif
▶️ How to Run
pip install -r requirements.txt
streamlit run Diamond_app.py

---

## 📊 Visualizations

| Plot | Description |
|------|------------|
| 📉 Scatter Plot | Carat vs Price with clusters |
| 📊 Histogram | Price distribution with predicted price |
| 📦 Bar Chart | Cluster distribution |

---

## 👤 Author

Pooja Reddy Nedhunuri
🎓 Capstone Project – Diamond Dynamics




