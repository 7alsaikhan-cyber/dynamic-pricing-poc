import streamlit as st
import time
from datetime import datetime
import pytz

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Dynamic Pricing Engine", layout="centered")

# --- Auto Refresh (every 60 seconds) ---
time.sleep(60)
st.experimental_rerun()

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
    rationale = (
        f"Competitor is selling higher at {competitor_price:.0f} SAR. "
        f"Raise our price to stay 2% below → {suggested:.0f} SAR."
    )
elif competitor_price < our_price:
    suggested = competitor_price
    action = "⬇️ Decrease"
    rationale = (
        f"Competitor is cheaper ({competitor_price:.0f} SAR). "
        f"Lower our price to match → {suggested:.0f} SAR."
    )
else:
    suggested = our_price
    action = "⏸️ No Change"
    rationale = "Our price is already aligned with competitor."

# --- Display Results ---
st.divider()
st.metric("💡 Action", action)
st.metric("💰 Suggested Price", f"{suggested:.0f} SAR")
st.metric("🏷️ Our Current Price", f"{our_price:.0f} SAR")
st.metric("🏪 Competitor Price", f"{competitor_price:.0f} SAR")
st.write("**Reason:**", rationale)

# --- Timestamp (Riyadh Time) ---
ksa_time = datetime.now(pytz.timezone("Asia/Riyadh")).strftime("%I:%M:%S %p – %d %b %Y")
st.caption(f"🕒 Last updated: {ksa_time} (Riyadh time)")

st.caption("Proof of Concept – Channels by stc 2025")
