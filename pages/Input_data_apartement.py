import streamlit as st
from spk_main import apartments
from spk_data import save_apartments
# C1 criteria - single choice radios
name = st.text_input("Apartment Name")
harga_beli = st.radio("Harga Beli", [
    'Premium (> Rp1,2 miliar)',
    'Menengah Atas (Rp800 juta – Rp1,2 miliar)',
    'Menengah (Rp500 juta – Rp800 juta)',
    'Ekonomis (< Rp500 juta)'
])

harga_sewa = st.radio("Harga Sewa", [
    'Premium (> Rp8 juta/bulan)',
    'Menengah Atas (Rp5 juta – Rp8 juta/bulan)',
    'Menengah (Rp3 juta – Rp5 juta/bulan)',
    'Ekonomis (< Rp3 juta/bulan)'
])

biaya_perawatan = st.radio("Biaya Perawatan", [
    'Tinggi (> Rp1 juta/bulan)',
    'Sedang (Rp500 ribu – Rp1 juta/bulan)',
    'Rendah (< Rp500 ribu/bulan)'
])

# C2 criteria - single choice radios
lokasi = st.radio("Lokasi", [
    'Strategis (Pusat kota/Pusat bisnis)',
    'Semi-strategis (Area pengembangan/Dekat fasilitas publik)',
    'Pinggiran (Kawasan pinggiran kota)',
    'Pedesaan (Jauh dari pusat kota)'
])

transportasi = st.radio("Transportasi", [
    'Sangat baik (Dekat stasiun/terminal, banyak transportasi online)',
    'Baik (Akses transportasi umum reguler)',
    'Cukup (Transportasi umum terbatas)',
    'Kurang (Transportasi sangat terbatas)'
])

fasilitas_publik = st.radio("Kedekatan dengan Fasilitas Publik", [
    'Sangat dekat (< 500 meter ke mal/supermarket/rumah sakit)',
    'Dekat (500m - 1km ke fasilitas publik)',
    'Sedang (1km - 3km ke fasilitas publik)',
    'Jauh (> 3km ke fasilitas publik)'
])

# C3 criteria - multiple choice checkboxes for Fasilitas Umum
st.write("Fasilitas Umum (Pilih semua yang tersedia):")
fasilitas_umum_options = [
    'Kolam renang', 'Gym', 'Taman', 'Parkir', 'Sauna', 'Playground', 'Ruang serba guna'
]
fasilitas_umum = []
for option in fasilitas_umum_options:
    if st.checkbox(option):
        fasilitas_umum.append(option)

# C3 criteria - multiple choice checkboxes for Fasilitas Unit
st.write("Fasilitas Unit (Pilih semua yang tersedia):")
fasilitas_unit_options = [
    'Smart Home Features', 'AC (Air Conditioner)', 'Water Heater', 
    'Built-in Furniture', 'Dapur Terpisah', 'Listrik dan Air Terjamin', 'Unit Kosong (no extras)'
]
fasilitas_unit = []
for option in fasilitas_unit_options:
    if st.checkbox(option):
        fasilitas_unit.append(option)

# C3 - Luas Unit (single choice)
luas_unit = st.radio("Luas Unit", [
    'Besar (> 80m²)',
    'Sedang (50m² - 80m²)',
    'Kecil (30m² - 50m²)',
    'Studio (< 30m²)'
])

# C4 criteria - single choice radios
sistem_keamanan = st.radio("Sistem Keamanan", [
    'Sangat lengkap (Keamanan 24 jam, CCTV, kartu akses, fingerprint)',
    'Lengkap (Keamanan 24 jam, CCTV, kartu akses)',
    'Standar (Satpam 24 jam)',
    'Minimal (Satpam tidak 24 jam)'
])

keamanan_lingkungan = st.radio("Keamanan Lingkungan", [
    'Sangat aman (Kawasan elit, crime rate rendah)',
    'Aman (Kawasan residensial, keamanan terjaga)',
    'Cukup aman (Area umum, tingkat kejahatan rata-rata)',
    'Kurang aman (Area rawan, tingkat kejahatan tinggi)'
])

fire_safety = st.radio("Fire Safety", [
    'Sangat baik (Sprinkler, alarm, tangga darurat, latihan berkala)',
    'Baik (Sprinkler, alarm, tangga darurat)',
    'Cukup (Alarm dan tangga darurat)',
    'Kurang (Standar minimal)'
])

# C5 criteria - single choice radios
capital_gain = st.radio("Capital Gain", [
    'Sangat tinggi (Pertumbuhan nilai >15% per tahun)',
    'Tinggi (Pertumbuhan nilai 10-15% per tahun)',
    'Sedang (Pertumbuhan nilai 5-10% per tahun)',
    'Rendah (Pertumbuhan nilai <5% per tahun)'
])

rental_yield = st.radio("Rental Yield", [
    'Sangat tinggi (>8% per tahun)',
    'Tinggi (6-8% per tahun)',
    'Sedang (4-6% per tahun)',
    'Rendah (<4% per tahun)'
])

prospek_area = st.radio("Prospek Area", [
    'Sangat baik (Area berkembang pesat, proyek infrastruktur baru)',
    'Baik (Area berkembang)',
    'Cukup (Area stabil)',
    'Kurang (Area stagnan/menurun)'
])

# Button to save apartment data
if st.button("Save Apartment Data"):
    if not name:
        st.error("Please enter the apartment name")
    else:
        apartment_data = {
            'Harga Beli': harga_beli,
            'Harga Sewa': harga_sewa,
            'Biaya Perawatan': biaya_perawatan,
            'Lokasi': lokasi,
            'Transportasi': transportasi,
            'Kedekatan dengan Fasilitas Publik': fasilitas_publik,
            'Fasilitas Umum': fasilitas_umum,
            'Fasilitas Unit': fasilitas_unit,
            'Luas Unit': luas_unit,
            'Sistem Keamanan': sistem_keamanan,
            'Keamanan Lingkungan': keamanan_lingkungan,
            'Fire Safety': fire_safety,
            'Capital Gain': capital_gain,
            'Rental Yield': rental_yield,
            'Prospek Area': prospek_area
        }

        apartments.append({
            'name': name,
            'data': apartment_data
        })
        save_apartments(apartments)
        st.success(f"Apartment '{name}' saved!")
