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
    return pd.read_csv("air_quality_dataset.csv")

df = load_data()

menu = st.sidebar.radio("Menu", ["Home", "EDA", "Visualization", "Modeling", "Prediction"])

if menu == "Home":
    st.title("Prediksi Kualitas Udara")
    st.subheader("Aplikasi untuk memprediksi kualitas udara berdasarkan data historis.")
    st.write("Selamat datang di aplikasi prediksi kualitas udara! Aplikasi ini menggunakan data historis untuk memprediksi kualitas udara di masa depan. Silakan pilih menu di sidebar untuk mulai menjelajahi data dan model prediksi.")
elif menu == "EDA":
    eda.show(df)
elif menu == "Visualization":
    visualization.show(df)
elif menu == "Modeling":
    modeling.show(df)
elif menu == "Prediction":
    prediction.show(df)