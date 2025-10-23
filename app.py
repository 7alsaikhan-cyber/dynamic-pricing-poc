import streamlit as st
from datetime import datetime, timedelta
import time

# --- Streamlit Page Config ---
st.set_page_config(page_title="AI Dynamic Pricing Engine", layout="centered")

# --- Header ---
st.markdown("""
<div style='text-align: center;'>
    <h2>Channels by stc – AI Dynamic Pricing Engine</h2>
    <h4>Hackathon Proof of Concept (PoC)</h4>
</div>
""", unsafe_allow_html=True)

# --- User Inputs ---
our_price = st.number_input("💰 Our Current Price (SAR)", value=519.0, step=1.0)
competitor_price = st.number_input("🏪 Competitor Price (SAR)", value=649.0, step=1.0)
discount_margin = 0.02  # 2% cheaper logic

# --- Core Logic ---
if competitor_price > our_price:
    suggested = competitor_price * (1 - discount_margin)
    action = "⬆️ Increase"
    rationale = f"Competitor is higher ({competitor_price:.0f} SAR). Raise price but stay 2% below → {suggested:.0f} SAR."
elif competitor_price < our_price:
    suggested = competitor_price * (1 - discount_margin)
    action = "⬇️ Decrease"
    rationale = f"Competitor is lower ({competitor_price:.0f} SAR). Drop price to 2% below → {suggested:.0f} SAR."
else:
    suggested = our_price
    action = "⚖️ Keep Same"
    rationale = "Price matches competitor – no change."

# --- Display Results ---
st.divider()
st.subheader("💡 Action")
st.write(f"{action}")
st.metric("💰 Suggested Price", f"{suggested:.0f} SAR")
st.metric("🏷️ Our Current Price", f"{our_price:.0f} SAR")
st.metric("🏪 Competitor Price", f"{competitor_price:.0f} SAR")
st.write(f"🧠 **Rationale:** {rationale}")

# --- Auto Refresh Section ---
refresh_interval = 300  # seconds (5 minutes)
next_refresh = datetime.now() + timedelta(seconds=refresh_interval)

st.divider()
st.markdown(f"🔄 **Auto-refresh enabled.** Next update at: {next_refresh.strftime('%I:%M_
