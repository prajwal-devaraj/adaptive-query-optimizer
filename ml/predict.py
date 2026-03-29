import os
import joblib
from ml.feature_extractor import feature_vector

MODEL_PATH = "ml/model.pkl"


def predict_runtime(query: str):
    if not os.path.exists(MODEL_PATH):
        return None
    model = joblib.load(MODEL_PATH)
    vector, features = feature_vector(query)
    predicted = float(model.predict([vector])[0])
    return predicted, features