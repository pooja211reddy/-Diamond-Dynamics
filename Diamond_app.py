import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import plotly.express as px
# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Diamond Dynamics",
    page_icon="💎",
    layout="centered"
)

# =========================
# LOAD FILES
# =========================
model = joblib.load("best_model.pkl")
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("cluster_scaler.pkl")
features = joblib.load("cluster_features.pkl")
df_cluster = joblib.load("clustered_data.pkl")
# =========================
# CSS
# =========================
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #8be9fd;
}
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #cfcfcf;
    margin-bottom: 30px;
}
.result-card {
    padding: 22px;
    border-radius: 18px;
    background: linear-gradient(135deg, #123524, #1f5c3a);
    color: white;
    font-size: 22px;
    font-weight: 700;
    margin-top: 18px;
}
.info-card {
    padding: 22px;
    border-radius: 18px;
    background: linear-gradient(135deg, #102a43, #1d4e89);
    color: white;
    font-size: 22px;
    font-weight: 700;
    margin-top: 18px;
}
.stButton>button {
    width: 100%;
    border-radius: 14px;
    height: 50px;
    font-size: 18px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown('<div class="main-title">💎 Diamond Dynamics</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Price Prediction & Market Segmentation System</div>', unsafe_allow_html=True)

# =========================
# INPUT SECTION
# =========================
st.markdown("### 🔹 Enter Diamond Details")

col1, col2 = st.columns(2)

with col1:
    carat = st.number_input("Carat", min_value=0.1, max_value=5.0, value=0.81, step=0.01)
    depth = st.number_input("Depth", min_value=40.0, max_value=80.0, value=61.9, step=0.1)
    table = st.number_input("Table", min_value=40.0, max_value=80.0, value=60.0, step=0.1)
    

with col2:
    x = st.number_input("Length (x)", min_value=0.1, max_value=15.0, value=5.91, step=0.01)
    y = st.number_input("Width (y)", min_value=0.1, max_value=15.0, value=5.86, step=0.01)
    z = st.number_input("Height (z)", min_value=0.1, max_value=15.0, value=3.64, step=0.01)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"], index=3)
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"], index=5)
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"], index=3)

# =========================
# ENCODING
# =========================
cut_map = {"Fair":0, "Good":1, "Very Good":2, "Premium":3, "Ideal":4}
color_map = {"D":0, "E":1, "F":2, "G":3, "H":4, "I":5, "J":6}
clarity_map = {"I1":0, "SI2":1, "SI1":2, "VS2":3, "VS1":4, "VVS2":5, "VVS1":6, "IF":7}

volume = x * y * z

input_dict = {
    "carat": carat,
    "cut": cut_map[cut],
    "color": color_map[color],
    "clarity": clarity_map[clarity],
    "depth": depth,
    "table": table,
    "x": x,
    "y": y,
    "z": z,
    "volume": volume
}

input_df = pd.DataFrame([input_dict])

# =========================
# BUTTONS
# =========================
st.markdown("---")

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    predict_price = st.button("💰 Predict Price")

with col_btn2:
    predict_cluster = st.button("📊 Predict Market Segment")

# =========================
# PRICE PREDICTION
# =========================
if predict_price:
    price_features = ["carat", "cut", "color", "clarity", "depth", "table", "volume"]
    price_input = input_df[price_features]

    pred_log = model.predict(price_input)[0]
    pred_price_usd = np.expm1(pred_log)
    pred_price_inr = pred_price_usd * 83

    st.markdown(
        f"""
        <div class="result-card">
        💵 Predicted Price: ${pred_price_usd:,.2f}<br>
        🇮🇳 Predicted Price: ₹ {pred_price_inr:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("## 📊 Price Distribution Analysis")
    fig = px.histogram(
    df_cluster,
    x="price",
    nbins=50,
    title="Price Distribution"
    )
    
    # add vertical line
    fig.add_vline(
        x=pred_price_usd,
        line_color="red",
        line_width=3,
        annotation_text="Your Price"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("## 📊 Price Range")

    low = df_cluster['price'].quantile(0.33)
    high = df_cluster['price'].quantile(0.66)

    if pred_price_usd < low:
        st.success("💚 Budget Range")
    elif pred_price_usd < high:
        st.info("💙 Mid Range")
    else:
        st.warning("💎 Premium Range")
# =========================
# CLUSTER PREDICTION
# =========================
if predict_cluster:
    cluster_names = {
        3: "Affordable Small Diamonds",
        2: "Lower Mid-range Diamonds",
        1: "Mid-range Diamonds",
        4: "High Value Diamonds",
        0: "Premium Luxury Diamonds"
    }

    cluster_input = input_df[features]
    cluster_scaled = scaler.transform(cluster_input)
    cluster = kmeans.predict(cluster_scaled)[0]
    segment = cluster_names.get(cluster, "Unknown Segment")
    price_features = ["carat", "cut", "color", "clarity", "depth", "table", "volume"]
    price_input = input_df[price_features]
    pred_log = model.predict(price_input)[0]
    pred_price_usd = np.expm1(pred_log)
    pred_price_inr = pred_price_usd * 83
    st.markdown(
        f"""
        <div class="info-card">
        📊 Cluster: {cluster}<br>
        🏷️ Segment: {segment}
        </div>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown("## 🔍 Diamond Clusters")

    fig, ax = plt.subplots()

    ax.scatter(
        df_cluster['carat'],
        df_cluster['price'],
        c=df_cluster['cluster'],
        cmap='viridis',
        alpha=0.5
    )

    ax.scatter(
        input_df['carat'][0],
        pred_price_usd,
        color='red',
        s=120,
        label='Your Diamond'
    )

    ax.legend()
    st.pyplot(fig)

    st.markdown("## 📊 Cluster Distribution")

    cluster_counts = df_cluster['cluster'].value_counts().sort_index()

    fig = px.bar(
    x=cluster_counts.index,
    y=cluster_counts.values,
    labels={'x': 'Cluster', 'y': 'Count'},
    title="Number of Diamonds per Cluster",
    text=cluster_counts.values
    )

    fig.update_traces(marker_color='royalblue')
    fig.update_layout(title_x=0.3)  # center title

    st.plotly_chart(fig, use_container_width=True)

    

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Built with XGBoost, K-Means Clustering and Streamlit")