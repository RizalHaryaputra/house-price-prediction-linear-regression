# 🏡 Prediksi Harga Rumah dengan Linear Regression

Aplikasi web sederhana berbasis **Streamlit** untuk memprediksi harga rumah menggunakan model **Regresi Linear**.  
Model dilatih menggunakan dataset harga rumah dari Kaggle dan dapat memperkirakan harga berdasarkan 5 fitur utama.

---

## 📊 Fitur Aplikasi

- Prediksi harga rumah berdasarkan:
  1. Luas Bangunan (LB)
  2. Luas Tanah (LT)
  3. Jumlah Kamar Tidur (KT)
  4. Jumlah Kamar Mandi (KM)
  5. Ketersediaan Garasi (GRS)
- Tampilan antarmuka interaktif menggunakan **Streamlit**
- Model tersimpan dalam file `.pkl` yang dimuat secara otomatis
- Hasil prediksi ditampilkan dalam format **Rupiah (Rp)**

---

## 📁 Struktur Folder

```

📦 prediksi-harga-rumah-streamlit
├── models/
│   └── model_prediksi_harga_rumah.pkl
├── app.py
├── requirements.txt
└── README.md

```

---

## 📥 Dataset dan Model

- **Dataset:** [DATA_RUMAH.xlsx (Kaggle)](https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah?select=DATA+RUMAH.xlsx)
- **Notebook Pelatihan Model:** [Google Colab](https://colab.research.google.com/drive/1v5NQq30u80E_fJAq8o14m8t6LSUbWjCr?usp=sharing)

Model disimpan dalam folder `models` dengan nama:
```

model_prediksi_harga_rumah.pkl

````

---

## ⚙️ Cara Menjalankan Aplikasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/RizalHaryaputra/prediksi-harga-rumah-streamlit.git
   cd prediksi-harga-rumah-streamlit```

2. **Buat Virtual Environment (Opsional)**

   ```bash
   python -m venv venv
   source venv/bin/activate    # Mac / Linux
   venv\Scripts\activate       # Windows
   ```

3. **Instal Dependensi**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi**

   ```bash
   streamlit run app.py
   ```

---

## 📦 Dependensi Utama

* streamlit
* joblib
* numpy
* scikit-learn

Kamu dapat membuat file `requirements.txt` dengan perintah:

```bash
pip freeze > requirements.txt
```

---

## 🚀 Demo & Tampilan

Aplikasi menampilkan form input interaktif untuk mengisi detail properti, kemudian menampilkan hasil prediksi harga rumah berdasarkan model regresi linear yang telah dilatih.

---

## 🧠 Tentang Project

Project ini dibuat sebagai tugas **Praktikum Aplikasi Web** oleh:

**👤 Rizal Haryaputra**
NIM: 23051130013
Topik: *Prediksi Harga Rumah dengan Linear Regression*

---

## 📜 Lisensi

Proyek ini bersifat open-source dan dapat digunakan untuk keperluan pembelajaran.

```
