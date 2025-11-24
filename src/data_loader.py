import pandas as pd

def load_raw(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=["url","label"])
    df = df.drop_duplicates(subset=["url"])
    df["label"] = df["label"].astype(int)
    return df
