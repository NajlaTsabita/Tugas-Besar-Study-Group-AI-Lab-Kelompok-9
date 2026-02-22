import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def show(df):
    st.title("Prediksi Kualitas Udara")
    st.header("Visualisasi Data")
    st.write("Visualisasi untuk memahami distribusi dan hubungan antar variabel.")

    tab1, tab2, tab3 = st.tabs(["Visualisasi Univariat", "Visualisasi Bivariat", "Visualisasi Multivariat"])

    with tab1:
        st.subheader("Visualisasi Univariat")
        st.write("Visualisasi untuk melihat distribusi masing-masing variabel.")
        st.subheader("Histogram")
        menuHistogram = st.selectbox("Pilih Variabel Untuk Histogram", ["PM2.5", "PM10", "NOx", "NO2", "SO2", "CO", "CO2", "CH4", "VOCs", "Temperature", "Humidity"])
        if menuHistogram == "PM2.5":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["PM2.5"], kde=True)
            plt.title("Distribusi PM2.5")
            st.pyplot(fig)
        elif menuHistogram == "PM10":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["PM10"], kde=True)
            plt.title("Distribusi PM10")
            st.pyplot(fig)
        elif menuHistogram == "NOx":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["NOx"], kde=True)
            plt.title("Distribusi NOx")
            st.pyplot(fig)
        elif menuHistogram == "NO2":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["NO2"], kde=True)
            plt.title("Distribusi NO2")
            st.pyplot(fig)
        elif menuHistogram == "SO2":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["SO2"], kde=True)
            plt.title("Distribusi SO2")
            st.pyplot(fig)
        elif menuHistogram == "CO":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["CO"], kde=True)
            plt.title("Distribusi CO")
            st.pyplot(fig)
        elif menuHistogram == "CO2":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["CO2"], kde=True)
            plt.title("Distribusi CO2")
            st.pyplot(fig)
        elif menuHistogram == "CH4":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["CH4"], kde=True)
            plt.title("Distribusi CH4")
            st.pyplot(fig)
        elif menuHistogram == "VOCs":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["VOCs"], kde=True)
            plt.title("Distribusi VOCs")
            st.pyplot(fig)
        elif menuHistogram == "Temperature":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["Temperature"], kde=True)
            plt.title("Distribusi Temperature")
            st.pyplot(fig)
        elif menuHistogram == "Humidity":
            fig = plt.figure(figsize=(10, 6))
            sns.histplot(df["Humidity"], kde=True)
            plt.title("Distribusi Humidity")
            st.pyplot(fig)
    
        st.subheader("Boxplot")
        menuBoxplot = st.selectbox("Pilih Variabel untuk Boxplot", ["PM2.5", "PM10", "NOx", "NO2", "SO2", "CO", "CO2", "CH4", "VOCs", "Temperature", "Humidity"])
        if menuBoxplot == "PM2.5":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["PM2.5"], palette="Set2")
            plt.title("Boxplot PM2.5")
            st.pyplot(fig)
        elif menuBoxplot == "PM10":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["PM10"], palette="Set2")
            plt.title("Boxplot PM10")
            st.pyplot(fig)
        elif menuBoxplot == "NOx":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["NOx"], palette="Set2")
            plt.title("Boxplot NOx")
            st.pyplot(fig)
        elif menuBoxplot == "NO2":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["NO2"], palette="Set2")
            plt.title("Boxplot NO2")
            st.pyplot(fig)
        elif menuBoxplot == "SO2":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["SO2"], palette="Set2")
            plt.title("Boxplot SO2")
            st.pyplot(fig)
        elif menuBoxplot == "CO":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["CO"], palette="Set2")
            plt.title("Boxplot CO")
            st.pyplot(fig)
        elif menuBoxplot == "CO2":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["CO2"], palette="Set2")
            plt.title("Boxplot CO2")
            st.pyplot(fig)
        elif menuBoxplot == "CH4":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["CH4"], palette="Set2")
            plt.title("Boxplot CH4")
            st.pyplot(fig)
        elif menuBoxplot == "VOCs":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["VOCs"], palette="Set2")
            plt.title("Boxplot VOCs")
            st.pyplot(fig)
        elif menuBoxplot == "Temperature":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["Temperature"], palette="Set2")
            plt.title("Boxplot Temperature")
            st.pyplot(fig)
        elif menuBoxplot == "Humidity":
            fig = plt.figure(figsize=(10, 6))
            sns.boxplot(x=df["Location_Type"], y=df["Humidity"], palette="Set2")
            plt.title("Boxplot Humidity")
            st.pyplot(fig)

    with tab2:
        st.subheader("Visualisasi Bivariat")
        st.write("Visualisasi untuk melihat hubungan antara dua variabel.")
        st.subheader("Heatmap")
        num_cols = ['PM2.5', 'PM10', 'NOx', 'NO2', 'SO2', 'CO2', 'CH4', 'VOCs', 'Temperature', 'Humidity']
        fig = plt.figure(figsize=(12, 8))
        sns.heatmap(df[num_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Heatmap Korelasi Antar Variabel")
        st.pyplot(fig)

    with tab3:
        st.subheader("Visualisasi Multivariat")
        st.write("Visualisasi untuk melihat hubungan antara lebih dari dua variabel.")
        st.subheader("Pairplot")
        num_cols = ['PM2.5', 'PM10', 'NOx', 'NO2', 'SO2', 'CO2', 'CH4', 'VOCs', 'Temperature', 'Humidity']
        sns.pairplot(
            df[num_cols+['Location_Type']],
            hue='Location_Type',
            diag_kind='kde',
            plot_kws={'alpha':0.6},
            palette='Set2'
        )
        plt.suptitle("Pairplot Antar Variabel", y=1.02)
        st.pyplot(plt)

