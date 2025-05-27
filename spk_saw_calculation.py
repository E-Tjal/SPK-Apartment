import numpy as np
import pandas as pd

def normalize_matrix(matrix, criteria_types, weights):
    """
    Normalisasi matriks keputusan berdasarkan tipe kriteria (benefit/cost)
    """
    normalized = matrix.copy()
    for j in range(len(criteria_types)):
        if criteria_types[j] == 'Benefit':
            normalized.iloc[:, j] = matrix.iloc[:, j] / matrix.iloc[:, j].max()
        else:  # Cost
            normalized.iloc[:, j] = matrix.iloc[:, j].min() / matrix.iloc[:, j]
    return normalized

def calculate_preference(normalized_matrix, weights):
    """
    Menghitung nilai preferensi dengan mengalikan matriks ternormalisasi dengan bobot
    """
    return (normalized_matrix * weights).sum(axis=1)

def calculate_criteria_score(apartment_data, criteria_code, sub_criteria):
    """
    Menghitung skor untuk satu kriteria berdasarkan sub-kriteria
    """
    criteria_data = sub_criteria[criteria_code]
    total_score = 0
    
    for param in criteria_data:
        if param in apartment_data:
            if isinstance(apartment_data[param], dict):  # Untuk fasilitas yang bisa multiple
                for item in apartment_data[param]:
                    if item in criteria_data[param]:
                        total_score += criteria_data[param][item] * apartment_data[param][item]
            else:  # Untuk pilihan tunggal
                if apartment_data[param] in criteria_data[param]:
                    total_score += criteria_data[param][apartment_data[param]]
    
    return total_score

def perform_saw_analysis(apartments, criteria, sub_criteria):
    """
    Melakukan seluruh proses analisis SAW
    """
    # Membuat matriks keputusan
    decision_matrix = pd.DataFrame(index=[apt['name'] for apt in apartments], 
                                 columns=criteria.keys())
    
    criteria_types = [criteria[code]['type'] for code in criteria.keys()]
    weights = np.array([criteria[code]['weight'] for code in criteria.keys()])
    
    for i, apt in enumerate(apartments):
        for code in criteria.keys():
            decision_matrix.loc[apt['name'], code] = calculate_criteria_score(
                apt['data'], code, sub_criteria
            )
    
    # Normalisasi matriks
    normalized_matrix = normalize_matrix(decision_matrix, criteria_types, weights)
    
    # Hitung nilai preferensi
    preference_scores = calculate_preference(normalized_matrix, weights)
    
    # Urutkan hasil
    results = pd.DataFrame({
        'Apartemen': [apt['name'] for apt in apartments],
        'Skor Preferensi': preference_scores.values
    }).sort_values('Skor Preferensi', ascending=False)
    
    results['Ranking'] = range(1, len(results)+1)
    results['Skor Preferensi'] = results['Skor Preferensi'].round(4)
    
    return {
        'results': results,
        'decision_matrix': decision_matrix,
        'normalized_matrix': normalized_matrix.round(4),
        'weights': weights
    }