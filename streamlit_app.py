# streamlit_app.py
import streamlit as st
import requests

st.title("Diagnostic du Diabète")

st.sidebar.header("Paramètres du Patient")


def user_input_features():
    # Les noms des colonnes doivent correspondre exactement au dataset original
    pregnancies = st.sidebar.number_input("Grossesses", 0, 20, 1)
    glucose = st.sidebar.number_input("Glucose", 0, 200, 100)
    blood_pressure = st.sidebar.number_input("Pression Artérielle", 0, 150, 70)
    skin_thickness = st.sidebar.number_input("Épaisseur de la peau", 0, 100, 20)
    insulin = st.sidebar.number_input("Insuline", 0, 900, 80)
    bmi = st.sidebar.number_input("IMC (BMI)", 0.0, 70.0, 25.0)
    dpf = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
    age = st.sidebar.number_input("Âge", 1, 120, 30)

    data = {
        'Number of times pregnant': pregnancies,
        'Plasma glucose concentration a 2 hours in an oral glucose tolerance test': glucose,
        'Diastolic blood pressure (mm Hg)': blood_pressure,
        'Triceps skin fold thickness (mm)': skin_thickness,
        '2-Hour serum insulin (mu U/ml)': insulin,
        'Body mass index (weight in kg/(height in m)^2)': bmi,
        'Diabetes pedigree function': dpf,
        'Age (years)': age
    }
    return data


input_data = user_input_features()

if st.button("Prédire"):
    # Appel à l'API Flask
    response = requests.post("http://127.0.0.1:5000/predict", json=input_data)

    if response.status_code == 200:
        res = response.json()
        status = "Positif" if res['prediction'] == 1 else "Négatif"
        st.subheader(f"Résultat : {status}")
        st.write(f"Confiance : {res['probability']:.2%}")
    else:
        st.error("Erreur lors de la communication avec l'API.")