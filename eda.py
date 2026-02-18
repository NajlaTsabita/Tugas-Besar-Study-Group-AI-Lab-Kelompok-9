import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def show(df):
    st.title("Prediksi Kualitas Udara")
    st.header("Exploratory Data Analysis (EDA)")
    st.write("Analisis data untuk memahami distribusi dan hubungan antar variabel.")
    
    st.subheader("Ringkasan Data:")
    st.dataframe(df.head())

    st.subheader("Dimensi Data:")
    col1, col2 = st.columns(2)
    col1.metric("Jumlah Baris", df.shape[0])
    col2.metric("Jumlah Kolom", df.shape[1])

    st.subheader("Statistik Data:")
    st.write(df.describe())

    st.subheader("Tipe Data:")
    df_info = df.dtypes.astype(str).reset_index()
    df_info.columns = ["Nama Kolom", "Tipe Data"]
    st.dataframe(df_info, hide_index=True, width=300)

    st.subheader("Integritas Data:")
    non_negative_cols = ["PM2.5", "PM10", "NOx", "NO2", "SO2", "CO", "CO2", "CH4", 'VOCs', 'Humidity']
    anomalous_rows = df[df[non_negative_cols].lt(0).any(axis=1)]
    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Nilai Hilang", df.isnull().sum().sum())
    col2.metric("Jumlah Baris Duplikat", df.duplicated().sum())
    col3.metric("Jumlah Data Anomali", anomalous_rows.shape[0])
    st.write("Catatan: Data anomali dalam dataset ini merupakan baris yang memiliki nilai negatif pada kolom yang seharusnya tidak boleh negatif. Kolom yang tak boleh negatif meliputi PM2.5, PM10, NOx, NO2, SO2, CO, CO2, CH4, VOCs, dan Humidity.")