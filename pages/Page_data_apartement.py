import streamlit as st
from spk_main import apartments

# Konfigurasi halaman
st.set_page_config(
    page_title="Daftar Apartment",
    page_icon="📋",
    layout="wide"
)


st.title("Daftar Apartement")

def display_apartment_details(apartment):
    """Menampilkan detail apartemen dalam format yang rapi"""
    data = apartment['data']
    
    # Header dengan border
    st.markdown(f"""
    <div style="
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        background: #ffc432;
    ">
        <h2 style="margin:0;color:#2c3e50;">🏠 {apartment['name']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Grid layout untuk kriteria
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Kriteria Harga
        with st.expander("💰 **Harga**", expanded=False):
            st.table({
                "Parameter": ["Harga Beli", "Harga Sewa", "Biaya Perawatan"],
                "Nilai": [data['Harga Beli'], data['Harga Sewa'], data['Biaya Perawatan']]
            })
        
        # Kriteria Lokasi
        with st.expander("📍 **Lokasi**", expanded=False):
            st.table({
                "Parameter": ["Lokasi", "Transportasi", "Kedekatan Fasilitas"],
                "Nilai": [data['Lokasi'], data['Transportasi'], data['Kedekatan dengan Fasilitas Publik']]
            })
    
    with col2:
        # Kriteria Keamanan
        with st.expander("🔒 **Keamanan**", expanded=False):
            st.table({
                "Parameter": ["Sistem Keamanan", "Keamanan Lingkungan", "Fire Safety"],
                "Nilai": [data['Sistem Keamanan'], data['Keamanan Lingkungan'], data['Fire Safety']]
            })
        
        # Kriteria Investasi
        with st.expander("📈 **Investasi**", expanded=False):
            st.table({
                "Parameter": ["Capital Gain", "Rental Yield", "Prospek Area"],
                "Nilai": [data['Capital Gain'], data['Rental Yield'], data['Prospek Area']]
            })
    
    # Fasilitas (full width)
    with st.expander("🏊 **Fasilitas**", expanded=False):
        fac_col1, fac_col2 = st.columns(2)
        
        with fac_col1:
            st.subheader("Fasilitas Umum")
            if 'Fasilitas Umum' in data and data['Fasilitas Umum']:
                for facility in data['Fasilitas Umum']:
                    st.markdown(f"<div style='padding:5px;'>✓ {facility}</div>", unsafe_allow_html=True)
            else:
                st.markdown("❌ Tidak ada fasilitas umum")
        
        with fac_col2:
            st.subheader("Fasilitas Unit")
            if 'Fasilitas Unit' in data and data['Fasilitas Unit']:
                for facility in data['Fasilitas Unit']:
                    st.markdown(f"<div style='padding:5px;'>✓ {facility}</div>", unsafe_allow_html=True)
            else:
                st.markdown("❌ Tidak ada fasilitas unit")
    
    st.markdown("---")

st.title("📋 Data Apartemen")
st.write("Berikut adalah detail lengkap dari semua apartemen yang akan dinilai.")

# Buat atau ambil data apartemen dari session state
if 'apartments' not in st.session_state:
    # st.session_state.apartments = create_dummy_apartments()
    st.session_state.apartments = apartments

apartments = st.session_state.apartments

# Tampilkan semua apartemen
for apt in apartments:
    display_apartment_details(apt)

# Tombol kembali ke halaman utama
if st.button("← Kembali ke Halaman Utama"):
    st.switch_page("spk_main.py")