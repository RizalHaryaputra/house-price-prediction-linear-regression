# Unduh dataset dari Kaggle: https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah?select=DATA+RUMAH.xlsx
# Link Notebook untuk melatih model: https://colab.research.google.com/drive/1v5NQq30u80E_fJAq8o14m8t6LSUbWjCr?usp=sharing

import streamlit as st
import joblib
import numpy as np
import os

# 1. Muat Model yang Sudah Disimpan di dalam folder 'models'
model_path = os.path.join('models', 'model_prediksi_harga_rumah.pkl')
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error("Model file tidak ditemukan. Pastikan 'model_prediksi_harga_rumah.pkl' ada di folder 'models'.")
    st.stop()


st.set_page_config(page_title="Prediksi Harga Properti", layout="centered")

st.header('🏡 Prediksi Harga Properti')
st.write("Aplikasi untuk memprediksi harga rumah berdasarkan 5 fitur utama.")
st.markdown("---") 

# 2. Buat Input untuk 5 Fitur (X)

# Input harus sesuai dengan 5 fitur yang digunakan saat pelatihan: LB, LT, KT, KM, GRS.
st.header("Masukkan Detail Properti")

# Menggunakan kolom untuk tata letak yang lebih rapi
col1, col2 = st.columns(2)

with col1:
    # 1. Luas Bangunan (LB) - Satuan m²
    lb_input = st.number_input(
        '1. Luas Bangunan (LB) - m²', 
        min_value=30, 
        max_value=1000, 
        value=150, 
        step=5,
        help="Ukuran total bangunan rumah."
    )

    # 2. Luas Tanah (LT) - Satuan m²
    lt_input = st.number_input(
        '2. Luas Tanah (LT) - m²', 
        min_value=50, 
        max_value=2000, 
        value=200, 
        step=10,
        help="Ukuran total tanah properti."
    )
    
    # 3. Jumlah Kamar Tidur (KT)
    kt_input = st.slider(
        '3. Jumlah Kamar Tidur (KT)', 
        min_value=1, 
        max_value=7, 
        value=4,
        help="Jumlah ruangan tidur."
    )

with col2:
    # 4. Jumlah Kamar Mandi (KM)
    km_input = st.slider(
        '4. Jumlah Kamar Mandi (KM)', 
        min_value=1, 
        max_value=5, 
        value=3,
        help="Jumlah kamar mandi/toilet."
    )

    # 5. Garasi (GRS) - Ini harus di-encode menjadi angka (0 atau 1)
    grs_option = st.selectbox(
        '5. Ketersediaan Garasi (GRS)', 
        ('ADA', 'TIDAK ADA'),
        help="Pilih ketersediaan garasi. Model Anda mungkin menggunakan 1/0."
    )
    # Asumsi: Model Anda menggunakan 1 untuk 'ADA' dan 0 untuk 'TIDAK ADA'
    grs_encoded = 1 if grs_option == 'ADA' else 0

# 3. Tombol Prediksi
if st.button('Hitung Prediksi Harga'):

    # 4. Susun Input data sesuai urutan pelatihan model (LB, LT, KT, KM, GRS)
    data_input = np.array([[lb_input, lt_input, kt_input, km_input, grs_encoded]])

    # 5. Lakukan Prediksi
    # Gunakan try-except untuk menangani potential error jika model.predict gagal
    try:
        prediksi_harga_juta = model.predict(data_input)[0]
        
        # Mengembalikan hasil prediksi ke satuan Rupiah (dikali 1.000.000)
        prediksi_harga = prediksi_harga_juta * 1000000 

        # Pembulatan, karena harga tidak mungkin negatif
        prediksi_harga = max(0, prediksi_harga) 

        # 6. Tampilkan Hasil
        st.markdown("---")
        st.markdown("### Hasil Prediksi:")
        
        # Mengubah ke string dan memformat sebagai Rupiah dengan pemisah ribuan titik
        harga_rupiah = "Rp {0:,.0f}".format(prediksi_harga).replace(",", "#").replace(".", ",").replace("#", ".")
        
        st.success(f"Estimasi Harga Jual Properti:")
        st.metric(label="Nilai Prediksi", value=harga_rupiah)
        st.caption("Prediksi didasarkan pada model Regresi Linier yang dilatih.")

    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi. Pastikan data input sudah benar. Error: {e}")
