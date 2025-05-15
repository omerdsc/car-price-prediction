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

2. Terminalden çalıştırın.
python model_egit.py
ardından
streamlit run app.py
![Ekran görüntüsü 2025-05-15 161357](https://github.com/user-attachments/assets/a6e5ccf4-4a7e-495d-8f2e-0563f64ff0b1)
![Ekran görüntüsü 2025-05-15 161432](https://github.com/user-attachments/assets/6bcc3450-d2f2-4dc7-88b3-fd8e01014b7c)


