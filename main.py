from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import requests

model = joblib.load("fraud_model.pkl")
WEBHOOK_URL = "http://localhost:9000/alert"

app = FastAPI()

class Transaction(BaseModel):
    amount: float
    location: float
    transaction_type: float
    device_trust_score: float

def trigger_webhook(data):
    try:
        requests.post(WEBHOOK_URL, json=data)
    except:
        print("⚠️ Webhook failed (simulate alert)")

@app.post("/predict")
def predict(txn: Transaction):
    input_data = np.array([[txn.amount, txn.location, txn.transaction_type, txn.device_trust_score]])
    pred = model.predict(input_data)[0]
    result = "fraud" if pred == 1 else "safe"
    if result == "fraud":
        print("🚨 Fraud detected. Triggering webhook.")
        trigger_webhook(txn.dict())
    return {"status": result}
