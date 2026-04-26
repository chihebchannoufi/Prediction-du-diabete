# train.py
from pycaret.datasets import get_data
from pycaret.classification import setup, compare_models, finalize_model, save_model

# 1. Chargement des données
data = get_data('diabetes')

# 2. Configuration de l'environnement (AutoML)
# target='Class variable' est la colonne cible pour ce dataset
s = setup(data, target='Class variable', session_id=123, verbose=False)

# 3. Entraînement et sélection du meilleur modèle
best_model = compare_models()

# 4. Finalisation (entraînement sur l'ensemble des données)
final_model = finalize_model(best_model)

# 5. Sauvegarde du pipeline
save_model(final_model, 'diabetes_pipeline')