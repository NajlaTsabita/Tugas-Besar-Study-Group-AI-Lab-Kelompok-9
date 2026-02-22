import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import eda
import visualization
import modeling
import prediction


st.set_page_config(page_title="Prediksi Kualitas Udara", page_icon=":sparkles:", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("air_quality_dataset.csv")
    # Data cleaning
    non_negative_columns = ["PM2.5", "PM10", "NOx", "NO2", "SO2", "CO", "CO2", "CH4", "VOCs", "Humidity"]
    df[non_negative_columns] = df[non_negative_columns].clip(lower=0)
    return df

df = load_data()

menu = st.sidebar.radio("Menu", ["Home", "EDA", "Visualization", "Modeling", "Prediction"])

if menu == "Home":
    st.title("Prediksi Kualitas Udara")
    st.subheader("Aplikasi untuk memprediksi kualitas udara berdasarkan data historis.")
    
    st.write("Selamat datang di aplikasi prediksi kualitas udara! Aplikasi ini menggunakan data historis untuk memprediksi kualitas udara di masa depan. Silakan pilih menu di sidebar untuk mulai menjelajahi data dan model prediksi.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Ringkasan Data")
        st.metric("Jumlah Baris Data", df.shape[0])
        st.metric("Jumlah Kolom Data", df.shape[1])
        st.write("Data mencakup variabel seperti PM2.5, NOx, SO2, dan lainnya untuk analisis kualitas udara.")
    
    with col2:
        st.markdown("### Fitur Aplikasi")
        st.write("- **EDA**: Analisis eksplorasi data untuk memahami distribusi dan integritas data.")
        st.write("- **Visualization**: Visualisasi univariat, bivariat, dan multivariat untuk insight mendalam.")
        st.write("- **Modeling**: Pelatihan model Random Forest untuk regresi dan klasifikasi.")
        st.write("- **Prediction**: Prediksi konsentrasi PM2.5 atau tingkat risiko berdasarkan input pengguna.")
    
    st.markdown("---")
    

elif menu == "EDA":
    eda.show(df)
elif menu == "Visualization":
    visualization.show(df)
elif menu == "Modeling":
    modeling.show(df)
elif menu == "Prediction":
    prediction.show(df)