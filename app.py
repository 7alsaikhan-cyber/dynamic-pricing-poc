import streamlit as st
from datetime import datetime, timedelta
import time

# --- Page setup ---
st.set_page_config(page_title="AI Dynamic Pricing Engine", layout="centered")

# --- Header ---
st.markdown("""
<div style='text-align:center;'>
  <h2>Channels by stc – AI Dynamic Pricing Engine</h2>
  <h4>Hackathon Proof of Concept (PoC)</h4>
</div>
""", unsafe_allow_html=True)

# --- User inputs ---
our_price = st.number_input("💰 Our Current Price (SAR)", value=519.0, step=1.0)
competitor_price = st.number_input("🏪 Competitor Price (SAR)", value=649.0, step=1.0)
discount_margin = 0.02  # 2% below competitor

# --- Dynamic Pricing Logic ---
if competitor_price > our_price:
    suggested = competitor_price * (1 - discount_margin)
    action = "⬆️ Increase"
    rationale = f"Competitor sells higher ({competitor_price:.0f} SAR). Raise our price to stay 2% cheaper → {suggested:.0f} SAR."
elif competitor_price < our_price:
    suggested = competitor_price * (1 - discount_margin)
    action = "⬇️ Decrease"
    rationale = f"Competitor sells lower ({competitor_price:.0f} SAR). Drop our price to stay 2% cheaper → {suggested:.0f} SAR."
else:
    suggested = our_price
    action = "⏸ No Change"
    rationale = "Our price matches competitor."

# --- Display Results ---
st.divider()
st.metric("💡 Action", action)
st.metric("💰 Suggested Price", f"{suggested:.2f} SAR")
st.write(f"**Reason:** {rationale}")

# --- Auto-refresh every 5 minutes ---
refresh_interval = 5  # in minutes
next_refresh = datetime.now() + timedelta(minutes=refresh_interval)

st.markdown(
    f"🔄 **Auto-refresh enabled.** Next refresh at: {next_refresh.strftime('%I:%M %p')} "
)
st.toast("Refreshing data every 5 minutes...")

# Wait 5 minutes before refreshing
time.sleep(refresh_interval * 60)
st.rerun()
