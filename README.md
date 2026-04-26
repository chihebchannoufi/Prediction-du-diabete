# Projet Data Science - Prédiction du diabète

Ce projet propose une application complète de prédiction du diabète avec:
- un script d'entraînement AutoML (PyCaret),
- une API Flask pour servir le modèle,
- une interface Streamlit pour saisir les données patient et afficher le résultat.

## Structure du projet

- `train.py`: entraîne et sauvegarde le pipeline de modèle (`diabetes_pipeline.pkl`).
- `app.py`: expose une route API `POST /predict` sur `http://127.0.0.1:5000`.
- `streamlit_app.py`: interface utilisateur Streamlit qui appelle l'API Flask.

## Prérequis

- Python 3.9+ (recommandé)
- Un environnement virtuel (`venv`)
- Dépendances Python:
  - `pycaret`
  - `flask`
  - `pandas`
  - `streamlit`
  - `requests`

## Installation

1. Créer et activer un environnement virtuel:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Installer les dépendances:

```powershell
pip install pycaret flask pandas streamlit requests
```

## Exécution

### 1) Entraîner le modèle (si nécessaire)

```powershell
python train.py
```

Cette commande génère le fichier `diabetes_pipeline.pkl`.

### 2) Lancer l'API Flask

```powershell
python app.py
```

API disponible sur: `http://127.0.0.1:5000/predict`

### 3) Lancer l'interface Streamlit

Dans un second terminal:

```powershell
streamlit run streamlit_app.py
```

L'interface envoie les données à l'API Flask et affiche:
- le diagnostic (`Positif` ou `Négatif`),
- la probabilité associée.

## Exemple de requête API

```json
{
  "Number of times pregnant": 2,
  "Plasma glucose concentration a 2 hours in an oral glucose tolerance test": 120,
  "Diastolic blood pressure (mm Hg)": 70,
  "Triceps skin fold thickness (mm)": 20,
  "2-Hour serum insulin (mu U/ml)": 80,
  "Body mass index (weight in kg/(height in m)^2)": 25.1,
  "Diabetes pedigree function": 0.5,
  "Age (years)": 30
}
```

## Notes

- Le fichier de modèle est chargé dans `app.py` via `load_model('diabetes_pipeline')`.
- Assurez-vous que le modèle est entraîné avant d'appeler l'API.
- Le mode `debug=True` est activé dans Flask pour le développement.
