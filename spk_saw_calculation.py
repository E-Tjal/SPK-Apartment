# spk_saw_calculation.py

import numpy as np
import pandas as pd

def normalize_matrix(matrix, criteria_types, weights):
    """
    Normalisasi matriks keputusan berdasarkan tipe kriteria (benefit/cost)
    """
    normalized = matrix.copy()
    for j in range(len(criteria_types)):
        if criteria_types[j] == 'Benefit':
            # Handle potential division by zero if a column has all zeros
            if matrix.iloc[:, j].max() != 0:
                normalized.iloc[:, j] = matrix.iloc[:, j] / matrix.iloc[:, j].max()
            else:
                normalized.iloc[:, j] = 0 
        else:  # Cost
            # Handle potential division by zero if a column has all zeros
            if matrix.iloc[:, j].min() != 0:
                normalized.iloc[:, j] = matrix.iloc[:, j].min() / matrix.iloc[:, j]
            else:
                normalized.iloc[:, j] = 0 
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
    criteria_data_for_code = sub_criteria[criteria_code] # Get the specific sub-criteria for C1, C2, etc.
    total_score = 0

    # Iterate through each parameter within the current criteria_code (e.g., 'Harga Beli', 'Harga Sewa' for C1)
    for param_name, param_values_and_scores in criteria_data_for_code.items():
        if param_name in apartment_data:
            user_selected_value = apartment_data[param_name]

            if isinstance(user_selected_value, list): # This handles 'Fasilitas Umum' and 'Fasilitas Unit'
                for selected_item in user_selected_value:
                    if selected_item in param_values_and_scores: # Check if the selected item exists in our scoring data
                        total_score += param_values_and_scores[selected_item]
            else: 
                if user_selected_value in param_values_and_scores: # Check if the selected value exists in our scoring data
                    total_score += param_values_and_scores[user_selected_value]

    return total_score


def perform_saw_analysis(apartments, criteria, sub_criteria):
    """
    Melakukan seluruh proses analisis SAW
    """
    if not apartments: # Handle case where there are no apartments
        st.warning("Tidak ada data apartemen untuk dianalisis. Silakan tambahkan data apartemen terlebih dahulu.")
        return {
            'results': pd.DataFrame(columns=['Apartemen', 'Skor Preferensi', 'Ranking']),
            'decision_matrix': pd.DataFrame(),
            'normalized_matrix': pd.DataFrame(),
            'weights': np.array([])
        }


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