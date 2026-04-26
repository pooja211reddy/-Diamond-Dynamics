# 💎 Diamond Dynamics  
### 🚀 Price Prediction & Market Segmentation using Machine Learning  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
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

## 🚀 Features

- 💰 Real-time price prediction (USD & INR)  
- 📊 Market segmentation using clustering  
- 📈 Interactive visualizations:
  - Carat vs Price scatter plot  
  - Price distribution with prediction highlight  
  - Cluster distribution bar chart  
- 🎯 User input-based predictions  
- 🎨 Clean and modern UI  

---

## 🧠 Machine Learning Models

### 🔹 Price Prediction Model
- Model: **XGBoost Regressor**
- Target: `log(price)`
- Performance:
  - 📉 MAPE: **~6.79%**
  - 🎯 Accuracy: **~93.2%**

---

### 🔹 Market Segmentation Model
- Model: **K-Means Clustering (k=5)**

**Features Used:**
- carat  
- cut  
- color  
- clarity  
- depth  
- table  
- volume  

**Segments:**
- 🟢 Affordable Small Diamonds  
- 🔵 Mid-range Diamonds  
- 🟡 High Value Diamonds  
- 🔴 Premium Luxury Diamonds  
- ⚪ Very Cheap Tiny Diamonds  

---

## 📊 Visualizations

| Plot | Description |
|------|------------|
| 📉 Scatter Plot | Carat vs Price with clusters |
| 📊 Histogram | Price distribution with predicted price |
| 📦 Bar Chart | Cluster distribution |

---

## 🖥️ Streamlit App

### 🔹 Inputs
- Carat  
- Cut  
- Color  
- Clarity  
- Dimensions  

### 🔹 Outputs
- 💰 Predicted Price  
- 📊 Cluster ID  
- 🏷️ Market Segment  

---

## ⚙️ Tech Stack

- Python 🐍  
- Pandas & NumPy  
- Scikit-learn  
- XGBoost  
- Plotly & Matplotlib  
- Streamlit  

---

## 📂 Project Structure
