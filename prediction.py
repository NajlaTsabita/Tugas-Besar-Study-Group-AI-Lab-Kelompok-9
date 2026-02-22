import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

@st.cache_resource
def train_regression_model(df):
    features = ["SO2", "NO2", "VOCs", "Temperature"]
    X = df[features]
    y_reg = df["PM2.5"]
    X_train, _, y_train, _ = train_test_split(X, y_reg, test_size=0.2, random_state=42)
    rf_reg = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
    rf_reg.fit(X_train, y_train)
    return rf_reg

@st.cache_resource
def train_classification_model(df):
    features = ["SO2", "NO2", "VOCs", "Temperature"]
    X = df[features]
    q1 = df["PM2.5"].quantile(0.33)
    q2 = df["PM2.5"].quantile(0.66)
    def air_quality_label_data(pm25):
        if pm25 <= q1:
            return "Aman"
        elif pm25 <= q2:
            return "Sedang"
        else:
            return "Berbahaya"
    y_cls = df["PM2.5"].apply(air_quality_label_data)
    X_train, _, y_train, _ = train_test_split(X, y_cls, test_size=0.2, random_state=42, stratify=y_cls)
    rf_cls = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
    rf_cls.fit(X_train, y_train)
    return rf_cls

def show(df):
    st.title("Prediksi Kualitas Udara")
    st.markdown("Masukkan nilai fitur untuk mendapatkan prediksi konsentrasi PM2.5 atau tingkat risiko kualitas udara.")

    col1, col2 = st.columns(2)
    with col1:
        so2 = st.number_input("SO2 (µg/m³)", min_value=0.0, value=10.0, step=0.1)
        no2 = st.number_input("NO2 (µg/m³)", min_value=0.0, value=20.0, step=0.1)
    with col2:
        vocs = st.number_input("VOCs (µg/m³)", min_value=0.0, value=5.0, step=0.1)
        temp = st.number_input("Temperature (°C)", min_value=-50.0, value=25.0, step=0.1)

    input_data = pd.DataFrame([[so2, no2, vocs, temp]], columns=["SO2", "NO2", "VOCs", "Temperature"])

    tab1, tab2 = st.tabs(["Prediksi Regresi (PM2.5)", "Prediksi Klasifikasi (Risiko)"])

    with tab1:
        st.subheader("Prediksi Konsentrasi PM2.5")
        if st.button("Prediksi PM2.5"):
            rf_reg = train_regression_model(df)
            prediction = rf_reg.predict(input_data)[0]
            st.success(f"Prediksi Konsentrasi PM2.5: {prediction:.2f} µg/m³")

    with tab2:
        st.subheader("Prediksi Tingkat Risiko Kualitas Udara")
        if st.button("Prediksi Risiko"):
            rf_cls = train_classification_model(df)
            prediction = rf_cls.predict(input_data)[0]
            st.success(f"Prediksi Tingkat Risiko: {prediction}")
            if prediction == "Aman":
                st.info("Kualitas udara aman.")
            elif prediction == "Sedang":
                st.warning("Kualitas udara sedang, perhatikan kesehatan.")
            else:
                st.error("Kualitas udara berbahaya, hindari aktivitas luar.")