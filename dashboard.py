import streamlit as st
import json
from pathlib import Path
import os

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")
st.title("🚨 Real-Time Fraud Detection Dashboard")

# Use same path as webhook.py
ALERTS_FILE = Path(__file__).parent / "alerts.json"

# Debug info (collapsible)
with st.expander("🔧 Debug Information"):
    st.caption(f"📂 Reading alerts from: `{ALERTS_FILE}`")
    st.caption(f"File exists: {ALERTS_FILE.exists()}")
    st.caption(f"File size: {ALERTS_FILE.stat().st_size if ALERTS_FILE.exists() else 0} bytes")

# Display alerts
if not ALERTS_FILE.exists() or ALERTS_FILE.stat().st_size == 0:
    st.info("✅ No alerts received yet. Waiting for anomalies...")
else:
    try:
        alerts = json.loads(ALERTS_FILE.read_text())
    except json.JSONDecodeError:
        st.error("⚠️ Error reading alerts data!")
        st.stop()

    if not alerts:
        st.info("✅ All clear! No active alerts")
    else:
        st.success(f"📦 Total alerts received: {len(alerts)}")
        
        # Display metrics
        cols = st.columns(4)
        cols[0].metric("High Risk Alerts", sum(a['device_trust_score'] < 0.3 for a in alerts))
        cols[1].metric("Total Amount", f"₹{sum(a['amount'] for a in alerts):,.2f}")
        cols[2].metric("Avg Location Score", f"{sum(a['location'] for a in alerts)/len(alerts):.2f}")
        cols[3].metric("Latest Alert", f"₹{alerts[0]['amount']:.2f}")

        # Display alerts table
        st.divider()
        st.subheader("📜 Alert Details")
        for i, alert in enumerate(alerts):
            with st.container():
                cols = st.columns([1, 3])
                cols[0].subheader(f"#{i+1}")
                with cols[1]:
                    st.progress(alert['device_trust_score'], text=f"Risk Score: {alert['device_trust_score']:.0%}")
                    st.write(f"💸 **Amount:** ₹{alert['amount']:,.2f}")
                    st.write(f"📍 **Location Anomaly:** {alert['location']:.2f}")
                    st.write(f"🏷️ **Transaction Risk:** {alert['transaction_type']:.2f}")
                st.divider()