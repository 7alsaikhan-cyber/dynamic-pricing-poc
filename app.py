import streamlit as st
import time
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="Dynamic Pricing Engine", layout="centered")

# --- Header ---
st.markdown("""
<div style='text-align: center;'>
    <h2>Channels by stc – AI Dynamic Pricing Engine</h2>
    <h4>Hackathon Proof of Concept (PoC)</h4>
</div>
""", unsafe_allow_html=True)

# --- Auto Refresh Logic ---
refresh_interval = 300  # every 5 minutes (in seconds)
next_refresh = datetime.now() + timedelta(seconds=refresh_interval)

st.info(f"⏰ Last refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
countdown_placeholder = st.empty()

for i in range(refresh_interval, 0, -1):
    mins, secs = divmod(i, 60)
    countdown_placeholder.write(f"🔄 Next auto-refresh in **{mins:02d}:{secs:02d}**")
    time.sleep(1)

st.rerun()  # safely refresh the app

# --- User Inputs ---
our_price = st.number_input("💰 Our Current Price (SAR)", value=519.0, step=1.0)
competitor_price = st.number_input("🏪 Competitor Price (SAR)", value=649.0, step=1.0)
discount_margin = 0.02  # 2% cheaper logic

# --- Core Logic ---
if c
