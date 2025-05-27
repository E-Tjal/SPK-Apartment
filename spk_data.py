import random

# Data kriteria
criteria = {
    'C1': {'name': 'Harga', 'type': 'Cost', 'weight': 0.25},
    'C2': {'name': 'Lokasi dan Aksesibilitas', 'type': 'Benefit', 'weight': 0.20},
    'C3': {'name': 'Fasilitas Apartemen', 'type': 'Benefit', 'weight': 0.25},
    'C4': {'name': 'Keamanan', 'type': 'Benefit', 'weight': 0.15},
    'C5': {'name': 'Potensi Investasi', 'type': 'Benefit', 'weight': 0.15}
}

# Sub-kriteria
sub_criteria = {
    'C1': {
        'Harga Beli': {
            'Premium (> Rp1,2 miliar)': 5,
            'Menengah Atas (Rp800 juta – Rp1,2 miliar)': 4,
            'Menengah (Rp500 juta – Rp800 juta)': 3,
            'Ekonomis (< Rp500 juta)': 2
        },
        'Harga Sewa': {
            'Premium (> Rp8 juta/bulan)': 5,
            'Menengah Atas (Rp5 juta – Rp8 juta/bulan)': 4,
            'Menengah (Rp3 juta – Rp5 juta/bulan)': 3,
            'Ekonomis (< Rp3 juta/bulan)': 2
        },
        'Biaya Perawatan': {
            'Tinggi (> Rp1 juta/bulan)': 5,
            'Sedang (Rp500 ribu – Rp1 juta/bulan)': 3,
            'Rendah (< Rp500 ribu/bulan)': 2
        }
    },
    'C2': {
        'Lokasi': {
            'Strategis (Pusat kota/Pusat bisnis)': 5,
            'Semi-strategis (Area pengembangan/Dekat fasilitas publik)': 4,
            'Pinggiran (Kawasan pinggiran kota)': 3,
            'Pedesaan (Jauh dari pusat kota)': 2
        },
        'Transportasi': {
            'Sangat baik (Dekat stasiun/terminal, banyak transportasi online)': 5,
            'Baik (Akses transportasi umum reguler)': 4,
            'Cukup (Transportasi umum terbatas)': 3,
            'Kurang (Transportasi sangat terbatas)': 2
        },
        'Kedekatan dengan Fasilitas Publik': {
            'Sangat dekat (< 500 meter ke mal/supermarket/rumah sakit)': 5,
            'Dekat (500m - 1km ke fasilitas publik)': 4,
            'Sedang (1km - 3km ke fasilitas publik)': 3,
            'Jauh (> 3km ke fasilitas publik)': 2
        }
    },
    'C3': {
        'Fasilitas Umum': {
            'Kolam renang': 1,
            'Gym': 1,
            'Taman': 1,
            'Parkir': 2,
            'Sauna': 1,
            'Playground': 1,
            'Ruang serba guna': 1
        },
        'Fasilitas Unit': {
            'Smart Home Features': 1,
            'AC (Air Conditioner)': 2,
            'Water Heater': 1,
            'Built-in Furniture': 1,
            'Dapur Terpisah': 1,
            'Listrik dan Air Terjamin': 3,
            'Unit Kosong (no extras)': 0
        },
        'Luas Unit': {
            'Besar (> 80m²)': 5,
            'Sedang (50m² - 80m²)': 4,
            'Kecil (30m² - 50m²)': 3,
            'Studio (< 30m²)': 2
        }
    },
    'C4': {
        'Sistem Keamanan': {
            'Sangat lengkap (Keamanan 24 jam, CCTV, kartu akses, fingerprint)': 5,
            'Lengkap (Keamanan 24 jam, CCTV, kartu akses)': 4,
            'Standar (Satpam 24 jam)': 3,
            'Minimal (Satpam tidak 24 jam)': 2
        },
        'Keamanan Lingkungan': {
            'Sangat aman (Kawasan elit, crime rate rendah)': 5,
            'Aman (Kawasan residensial, keamanan terjaga)': 4,
            'Cukup aman (Area umum, tingkat kejahatan rata-rata)': 3,
            'Kurang aman (Area rawan, tingkat kejahatan tinggi)': 2
        },
        'Fire Safety': {
            'Sangat baik (Sprinkler, alarm, tangga darurat, latihan berkala)': 5,
            'Baik (Sprinkler, alarm, tangga darurat)': 4,
            'Cukup (Alarm dan tangga darurat)': 3,
            'Kurang (Standar minimal)': 2
        }
    },
    'C5': {
        'Capital Gain': {
            'Sangat tinggi (Pertumbuhan nilai >15% per tahun)': 5,
            'Tinggi (Pertumbuhan nilai 10-15% per tahun)': 4,
            'Sedang (Pertumbuhan nilai 5-10% per tahun)': 3,
            'Rendah (Pertumbuhan nilai <5% per tahun)': 2
        },
        'Rental Yield': {
            'Sangat tinggi (>8% per tahun)': 5,
            'Tinggi (6-8% per tahun)': 4,
            'Sedang (4-6% per tahun)': 3,
            'Rendah (<4% per tahun)': 2
        },
        'Prospek Area': {
            'Sangat baik (Area berkembang pesat, proyek infrastruktur baru)': 5,
            'Baik (Area berkembang)': 4,
            'Cukup (Area stabil)': 3,
            'Kurang (Area stagnan/menurun)': 2
        }
    }
}

def create_dummy_apartments():
    """
    Membuat contoh apartemen dummy dengan kriteria random
    """
    dummy_names = [
        "The Luxe Residence",
        "Urban Heights",
        "Green Valley Apartments",
        "Central Park Living",
        "Harmony Suites"
    ]
    
    dummy_apartments = []
    
    for name in dummy_names:
        # Harga (C1)
        harga_beli = random.choice(list(sub_criteria['C1']['Harga Beli'].keys()))
        harga_sewa = random.choice(list(sub_criteria['C1']['Harga Sewa'].keys()))
        biaya_perawatan = random.choice(list(sub_criteria['C1']['Biaya Perawatan'].keys()))
        
        # Lokasi (C2)
        lokasi = random.choice(list(sub_criteria['C2']['Lokasi'].keys()))
        transportasi = random.choice(list(sub_criteria['C2']['Transportasi'].keys()))
        fasilitas_publik = random.choice(list(sub_criteria['C2']['Kedekatan dengan Fasilitas Publik'].keys()))
        
        # Fasilitas (C3)
        fasilitas_umum = {}
        for facility in sub_criteria['C3']['Fasilitas Umum']:
            if random.random() > 0.5:  # 50% chance untuk memiliki fasilitas
                fasilitas_umum[facility] = 1
                
        fasilitas_unit = {}
        for facility in sub_criteria['C3']['Fasilitas Unit']:
            if random.random() > 0.5:  # 50% chance untuk memiliki fasilitas
                fasilitas_unit[facility] = 1
                
        luas_unit = random.choice(list(sub_criteria['C3']['Luas Unit'].keys()))
        
        # Keamanan (C4)
        sistem_keamanan = random.choice(list(sub_criteria['C4']['Sistem Keamanan'].keys()))
        keamanan_lingkungan = random.choice(list(sub_criteria['C4']['Keamanan Lingkungan'].keys()))
        fire_safety = random.choice(list(sub_criteria['C4']['Fire Safety'].keys()))
        
        # Investasi (C5)
        capital_gain = random.choice(list(sub_criteria['C5']['Capital Gain'].keys()))
        rental_yield = random.choice(list(sub_criteria['C5']['Rental Yield'].keys()))
        prospek_area = random.choice(list(sub_criteria['C5']['Prospek Area'].keys()))
        
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
        
        dummy_apartments.append({
            'name': name,
            'data': apartment_data
        })
    
    return dummy_apartments