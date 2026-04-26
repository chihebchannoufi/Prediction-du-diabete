# app.py
from flask import Flask, request, jsonify
from pycaret.classification import load_model, predict_model
import pandas as pd

app = Flask(__name__)

# Charger le modèle sauvegardé
model = load_model('diabetes_pipeline')


@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données envoyées par Streamlit
    data = request.get_json()
    df = pd.DataFrame([data])

    # Faire la prédiction
    predictions = predict_model(model, data=df)

    # Extraire le label et le score (Label et Score sont les noms par défaut dans PyCaret 2.x/3.x)
    result = {
        "prediction": int(predictions['prediction_label'][0]),
        "probability": float(predictions['prediction_score'][0])
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000, debug=True)