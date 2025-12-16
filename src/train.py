import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
MODEL_DIR = Path("models")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

def load_data():
    dfs = []
    for file in RAW_DIR.glob("*.CSV"):
        df = pd.read_csv(file)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def main():
    df = load_data()

    df["timestamp"] = pd.to_datetime(
        df[["year","month","day","hour","minute","second"]],
        errors="coerce"
    )
    df = df.dropna(subset=["timestamp"]).sort_values("timestamp")

    for c in ["moisture0","moisture1","moisture2","moisture3"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df[["moisture0","moisture1","moisture2","moisture3"]] = (
        df[["moisture0","moisture1","moisture2","moisture3"]]
        .interpolate()
    )

    threshold = df["moisture0"].quantile(0.20)
    df["irrigation_needed"] = (df["moisture0"] < threshold).astype(int)

    X = df[["moisture0","moisture1","moisture2","moisture3","hour"]]
    y = df["irrigation_needed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression())
    ])

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    print(classification_report(y_test, preds))

    joblib.dump(model, MODEL_DIR / "model.joblib")
    df.to_csv(PROCESSED_DIR / "processed.csv", index=False)

    print("MODEL VE VERİ KAYDEDİLDİ")

if __name__ == "__main__":
    main()
