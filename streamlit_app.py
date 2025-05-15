import streamlit as st
import joblib
import pandas as pd

# Modeli yükle
model = joblib.load("arac_fiyat_modeli.pkl")

st.title("Araç Fiyat Tahmini Uygulaması 🚗")

year = st.number_input("Model Yılı", min_value=1990, max_value=2025, value=2015)
make = st.text_input("Marka", "Toyota")
model_arac = st.text_input("Model", "Corolla")
body = st.selectbox("Kasa Tipi", ["sedan", "suv", "coupe", "convertible", "wagon", "Other"])
transmission = st.selectbox("Vites Türü", ["automatic", "manual", "Other"])
odometer = st.number_input("Kilometre (odometer)", value=50000)
color = st.text_input("Dış Renk", "white")
interior = st.text_input("İç Renk", "black")

if st.button("Fiyat Tahmini Yap"):
    input_df = pd.DataFrame({
        "year": [year],
        "make": [make],
        "model": [model_arac],
        "body": [body],
        "transmission": [transmission],
        "odometer": [odometer],
        "color": [color],
        "interior": [interior]
    })

    tahmin = model.predict(input_df)[0]
    st.success(f"Tahmini Satış Fiyatı: ${int(tahmin):,}")
