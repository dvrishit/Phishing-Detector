import argparse
from src.data_loader import load_raw
from src.features import extract_features_series
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import joblib
import pandas as pd

def main(data_path, out_path):
    df = load_raw(data_path)
    X = extract_features_series(df["url"].astype(str))
    y = df["label"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=150,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:,1]

    print(classification_report(y_test, preds))
    print("ROC-AUC:", roc_auc_score(y_test, probs))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, preds))

    joblib.dump({"model":model, "meta":{"feature_names": list(X.columns)}}, out_path)
    print("Saved model to", out_path)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data/raw/urls.csv")
    p.add_argument("--out", default="models/rf_model.pkl")
    args = p.parse_args()
    main(args.data, args.out)
