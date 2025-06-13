import pandas as pd
import joblib
import requests
import time

# Load model & data
model = joblib.load("fraud_model.pkl")
df = pd.read_csv("synthetic_transactions.csv")

X = df[["amount", "location", "transaction_type", "device_trust_score"]]
y = df["is_fraud"]

# Simulate real-time stream
for index, row in df.iterrows():
    features = [row["amount"], row["location"], row["transaction_type"], row["device_trust_score"]]
    prediction = model.predict([features])

    if prediction[0] == 1:  # If flagged as fraud
        payload = {
            "amount": row["amount"],
            "location": row["location"],
            "transaction_type": row["transaction_type"],
            "device_trust_score": row["device_trust_score"]
        }
        response = requests.post("http://127.0.0.1:9000/alert", json=payload)
        print(f"🚨 Alert Sent | Status: {response.status_code} | Data: {payload}")
        time.sleep(1.5)
