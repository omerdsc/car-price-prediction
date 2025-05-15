# 🚗 Araç Fiyat Tahmin Sistemi

Bu proje, ikinci el araçların teknik ve görsel özelliklerini kullanarak **tahmini satış fiyatlarını** belirlemeyi amaçlayan bir makine öğrenmesi uygulamasıdır. Veri seti 550.000'den fazla araç kaydı içermektedir.

## 📌 Proje Özellikleri

- 🔍 Gerçek dünya verisi ile çalışıldı
- 🧹 Eksik veri temizleme ve özellik mühendisliği uygulandı
- 🧠 Model: `RandomForestRegressor`
- 🛠️ Scikit-learn Pipeline ile model + ön işleme birleştirildi
- 🌐 Streamlit ile web arayüzü geliştirildi

## 📊 Kullanılan Özellikler

- **Kategorik**: marka, model, trim, gövde tipi, şanzıman, dış ve iç renk
- **Sayısal**: yaş, kilometre, MMR (piyasa değeri), km/yaş oranı

## 📦 Kullanılan Kütüphaneler

- pandas, numpy
- scikit-learn
- streamlit
- pickle

## 🚀 Uygulamayı Çalıştırmak

1. Gerekli kütüphaneleri yükleyin:
```bash
2. Terminalden çalıştırın.
python veri_temizleme_model.py
ardından
streamlit run app.py
