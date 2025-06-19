import streamlit as st
import pandas as pd
from spk_data import criteria, sub_criteria, create_dummy_apartments,load_apartments
from spk_saw_calculation import perform_saw_analysis

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Sistem Rekomendasi Apartemen",  # Ini yang akan muncul di pojok kiri atas
    page_icon="🏢", 
    layout="wide"
)

st.title("🏢 Sistem Pendukung Keputusan Pemilihan Apartemen")
st.markdown("""
**Metode:** Simple Additive Weighting (SAW)
            
**Kriteria:**
1. Harga (Cost)
2. Lokasi dan Aksesibilitas (Benefit)
3. Fasilitas Apartemen (Benefit)
4. Keamanan (Benefit)
5. Potensi Investasi (Benefit)
""")

if st.sidebar.button("📋 Lihat Data Apartemen"):
    st.switch_page("pages/Page_data_apartement.py")
if st.sidebar.button("📋 input Data Apartemen"):
    st.switch_page("pages/Input_data_apartement.py")
# Input bobot kriteria
st.header("🔢 Pengaturan Bobot Kriteria")
st.write("Atur bobot untuk setiap kriteria (total harus 100%):")


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    c1_weight = st.slider("Harga (C1)", 0, 100, 25, key="c1_weight")
with col2:
    c2_weight = st.slider("Lokasi (C2)", 0, 100, 20, key="c2_weight")
with col3:
    c3_weight = st.slider("Fasilitas (C3)", 0, 100, 25, key="c3_weight")
with col4:
    c4_weight = st.slider("Keamanan (C4)", 0, 100, 15, key="c4_weight")
with col5:
    c5_weight = st.slider("Investasi (C5)", 0, 100, 15, key="c5_weight")

total_weight = c1_weight + c2_weight + c3_weight + c4_weight + c5_weight

st.write("Jika tidak ingin menggunakan salah satu kriteria, atur bobot kriteria yang tidak digunakan menjadi 0.")
if total_weight != 100:
    st.error(f"Total bobot harus 100% (Saat ini: {total_weight}%). Silakan sesuaikan kembali.")
    st.stop()

# Update bobot kriteria
criteria['C1']['weight'] = c1_weight / 100
criteria['C2']['weight'] = c2_weight / 100
criteria['C3']['weight'] = c3_weight / 100
criteria['C4']['weight'] = c4_weight / 100
criteria['C5']['weight'] = c5_weight / 100

# Pilihan untuk menggunakan data dummy atau input manual
# apartments = create_dummy_apartments()
apartments = load_apartments()

#Button Perhitungan
if st.button("🚀 Hitung Rekomendasi"):
    result = perform_saw_analysis(apartments, criteria, sub_criteria)
    
    # Tampilkan hasil
    st.header("🏆 Hasil Rekomendasi")
    top_5_results = result['results'].head(5)
    st.dataframe(top_5_results.set_index('Ranking'), use_container_width=True)
    
    # Visualisasi
    st.subheader("📊 Visualisasi Skor Preferensi")
    st.bar_chart(top_5_results.set_index('Apartemen')['Skor Preferensi'])
    
    # Rekomendasi terbaik
    best_apartment = result['results'].iloc[0]
    st.success(f"**🏅 Rekomendasi Terbaik:** {best_apartment['Apartemen']} dengan skor {best_apartment['Skor Preferensi']:.4f}")
    
    # Detail perhitungan
    with st.expander("🔍 Detail Perhitungan"):
        st.subheader("Matriks Keputusan Awal")
        st.dataframe(result['decision_matrix'], use_container_width=True)
        
        st.subheader("Matriks Ternormalisasi")
        st.dataframe(result['normalized_matrix'], use_container_width=True)
        
        st.subheader("Bobot Kriteria")
        weights_df = pd.DataFrame({
            'Kriteria': [criteria[code]['name'] for code in criteria.keys()],
            'Tipe': [criteria[code]['type'] for code in criteria.keys()],
            'Bobot': result['weights']
        })
        st.dataframe(weights_df, use_container_width=True, hide_index=True)
