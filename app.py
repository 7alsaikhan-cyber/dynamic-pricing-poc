import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Dynamic Pricing Engine", layout="centered")

# --- Header ---
st.markdown("""
<div style='text-align:center'>
    <h2>Channels by stc – AI Dynamic Pricing Engine</h2>
    <h4>Hackathon Proof of Concept (PoC)</h4>
</div>
""", unsafe_allow_html=True)

# --- Auto Refresh Setup ---
refresh_interval = 300  # seconds = 5 minutes
next_refresh = datetime.now() + timedelta(seconds=refresh_interval)

# --- User Inputs ---
our_price = st.number_input("💰 Our Current Price (SAR)", value=519.0, step=1.0)
competitor_price = st.number_input("🏪 Competitor Price (SAR)", value=649.0, step=1.0)
discount_margin = 0.02  # 2% cheaper logic

# --- Core Logic ---
if competitor_price > our_price:
    suggested = competitor_price * (1 - discount_margin)
    action = "⬆️ Increase"
    rationale = (
        f"Competitor sells higher ({competitor_price:.0f} SAR). "
        f"Raise to stay 2 % below at {suggested:.0f} SAR."
    )
elif competitor_price < our_price:
    suggested = competitor_price  # match competitor
    action = "⬇️ Decrease"
    rationale = (
        f"Competitor sells lower ({compet
