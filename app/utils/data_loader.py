import pandas as pd
import json

def load_logs():
    return pd.read_csv("data/processed/logs_sample.csv")

def load_json(file):
    with open(file, "r") as f:
        return json.load(f)