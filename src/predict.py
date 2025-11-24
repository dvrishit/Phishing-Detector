import joblib
import pandas as pd
from src.features import extract_features

def load_model(path="models/rf_model.pkl"):
    d = joblib.load(path)
    return d["model"], d["meta"]

def predict_one(url, path="models/rf_model.pkl"):
    model, meta = load_model(path)
    feats = extract_features(url)
    order = meta["feature_names"]
    X = pd.DataFrame([feats], columns=order)
    prob = float(model.predict_proba(X)[0][1])
    pred = int(prob >= 0.5)
    return {"prediction": pred, "probability": prob}
