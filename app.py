import streamlit as st
import pandas as pd

# --- Header ---
st.markdown("""
<div style='text-align: center;'>
    <img src='https://upload.wikimedia.org/wikipedia/commons/6/6f/Stc_logo.svg' width='160'/>
    <h2>Channels by stc – AI Dynamic Pricing Engine</h2>
    <h4>Hackathon Proof of Concept (PoC)</h4>
</div>
""", unsafe_allow_html=True)

# --- Logic ---
our_price = 519
competitor_price = 499
TARGET_UNDERCUT = 10
MAX_DISCOUNT = 0.08

target = competitor_price - TARGET_UNDERCUT
cap = our_price * (1 - MAX_DISCOUNT)
suggested = max(min(target, cap), 49)
rationale = f"Undercut competitor by {TARGET_UNDERCUT} SAR within {int(MAX_DISCOUNT*100)}% cap."

# --- Metrics Display ---
st.divider()
st.metric("Competitor (Jarir)", f"{competitor_price:.0f} SAR")
st.metric("Our Current Price", f"{our_price} SAR")
st.metric("Suggested Price", f"{suggested:.0f} SAR")

# --- Chart ---
st.divider()
st.write("### 📊 Price Comparison")
data = pd.DataFrame({
    "Category": ["Competitor (Jarir)", "Our Current Price", "Suggested Price"],
    "Price (SAR)": [competitor_price, our_price, suggested]
})
st.bar_chart(data.set_index("Category"))

# --- Rationale ---
st.divider()
st.write("### 💡 Rationale")
st.write(rationale)

# --- Footer ---
st.write("""
<hr>
<small><b>Next Phase Vision:</b><br>
• Integrate with Power BI for real-time updates.<br>
• Expand to multiple competitors (Jarir, Extra, Noon).<br>
• Add AI-based demand forecasting and price elasticity models.
</small>
""", unsafe_allow_html=True)
