🚨 Real-Time Fraud Detection Dashboard
A lightweight project using FastAPI and Streamlit to simulate and monitor fraudulent transactions in real-time. It mimics a real-world backend alerting system where simulated anomalies are sent to a webhook and displayed on a dashboard.

📦 Tech Stack

FastAPI – for receiving alerts (webhook)

Streamlit – for visualizing alerts on the dashboard

Python – for scripting and alert simulation

⚙️ Installation
# Clone the repository
git clone https://github.com/tanishikaubale/fraud-alert-dashboard.git
cd fraud-alert-dashboard

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   (For Windows)
source venv/bin/activate   (For Linux/Mac)
# Install dependencies
pip install -r requirements.txt
 OR
pip install fastapi uvicorn pydantic joblib
pip freeze > requirements.txt


📂 File Structure
anomaly_detector/
├── main.py
├── webhook.py
├── fraud_model.pkl
├── synthetic_transactions.csv
├── requirements.txt
└── README.md


=> How to Run the Project
Open 2 separate terminals and follow the steps:
# Start the FastAPI Backend
bash
uvicorn api_backend:app --port 9000 (copy this)
# Start the Streamlit Dashboard
bash
streamlit run dashboard.py (copy this)


=> How It Works
api_backend.py receives and stores them in alerts.json.

dashboard.py reads and displays these alerts in real-time on a live dashboard.

