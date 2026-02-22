import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, classification_report

def show(df):
    st.title("Modeling Kualitas Udara (Random Forest)")
    st.markdown("Menggunakan algoritma **Random Forest** dengan fitur yang telah lolos uji Multikolinearitas (VIF).")

    features = ["SO2", "NO2", "VOCs", "Temperature"]
    X = df[features]

    st.info(f"**Fitur Input (X) yang digunakan:** {', '.join(features)}")

    tab1, tab2 = st.tabs(["Task 1: Regresi (Prediksi Angka)", "Task 2: Klasifikasi (Tingkat Risiko)"])

    with tab1:
        st.subheader("Prediksi Konsentrasi PM2.5")
        
        # Target Y untuk regresi
        y_reg = df["PM2.5"]
        
        # Split Data
        X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
            X, y_reg, test_size=0.2, random_state=42
        )
        
        if st.button("Jalankan Model Regresi"):
            with st.spinner("Sedang melatih pohon keputusan..."):
                # Training Model
                rf_reg = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
                rf_reg.fit(X_train_reg, y_train_reg)
                y_pred_reg = rf_reg.predict(X_test_reg)
                
                # Evaluasi
                r2 = r2_score(y_test_reg, y_pred_reg)
                rmse = np.sqrt(mean_squared_error(y_test_reg, y_pred_reg))
                
            
                st.success("Training Selesai!")
                col1, col2 = st.columns(2)
                col1.metric("R² Score (Akurasi)", f"{r2:.4f}")
                col2.metric("RMSE (Rata-rata Error)", f"{rmse:.4f}")


    with tab2:
        st.subheader("Klasifikasi Kualitas Udara (Aman / Sedang / Berbahaya)")
        
        # Menghitung batas Quantile
        q1 = df["PM2.5"].quantile(0.33)
        q2 = df["PM2.5"].quantile(0.66)
        
        # Fungsi Pelabelan
        def air_quality_label_data(pm25):
            if pm25 <= q1:
                return "Aman"
            elif pm25 <= q2:
                return "Sedang"
            else:
                return "Berbahaya"
                
        y_cls = df["PM2.5"].apply(air_quality_label_data)
        
        # Split Data dengan parameter stratify
        X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
            X, y_cls, test_size=0.2, random_state=42, stratify=y_cls
        )
        
        if st.button("Jalankan Model Klasifikasi"):
            with st.spinner("Sedang mengklasifikasikan risiko..."):
                # Training Model (Main Model)
                rf_cls = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
                rf_cls.fit(X_train_cls, y_train_cls)
                y_pred_cls = rf_cls.predict(X_test_cls)
                
                # Evaluasi
                acc = accuracy_score(y_test_cls, y_pred_cls)
                
            
                st.success("Training Selesai!")
                st.metric("Tingkat Akurasi Model", f"{acc:.2%}")
                
                
                st.text("Detailed Classification Report:")
                st.code(classification_report(y_test_cls, y_pred_cls))