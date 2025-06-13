from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
from pathlib import Path

app = FastAPI()

# Define absolute path for alerts.json (safer for file operations)
ALERTS_FILE = Path(__file__).parent / "alerts.json"

class Alert(BaseModel):
    amount: float
    location: float
    transaction_type: float
    device_trust_score: float

@app.post("/alert")
async def receive_alert(alert: Alert):
    print(f"📩 Received Alert: {alert.model_dump()}")

    # Create file if doesn't exist
    ALERTS_FILE.touch(exist_ok=True)
    
    # Read existing alerts
    try:
        alerts = json.loads(ALERTS_FILE.read_text())
    except (json.JSONDecodeError, FileNotFoundError):
        alerts = []

    # Add new alert (prepend for reverse chronological order)
    alerts.insert(0, alert.model_dump())

    # Write back to file
    ALERTS_FILE.write_text(json.dumps(alerts, indent=2))
    
    return {"message": "Alert received"}