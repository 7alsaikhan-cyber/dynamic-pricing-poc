import streamlit as st

st.set_page_config(page_title="Dynamic Pricing Engine", layout="centered")

# --- Header ---
st.markdown("""
<div style='text-align: center;'>
    <h2>Channels by stc – AI Dynamic Pricing Engine</h2>
    <h4>Hackathon Proof of Concept (PoC)</h4>
</div>
""", unsafe_allow_html=True)

# --- User inputs ---
our_price = st.number_input("💰 Our Current Price (SAR)", value=519.0, step=1.0)
competitor_price = st.number_input("🏪 Competitor Price (SAR)", value=649.0, step=1.0)
discount_margin = 0.02  # 2% cheaper logic

# --- Core logic ---
if competitor_price > our_price:
    # Competitor sells higher → we raise but stay 2% below
    suggested = competitor_price * (1 - discount_margin)
    action = "⬆️ Increase"
    rationale = (
        f"Competitor is selling higher at {competitor_price:.0f} SAR. "
        f"Raise our price to stay 2% below → {suggested:.0f} SAR."
    )

elif competitor_price < our_price:
    # Competitor sells cheaper → we lower our price to match within 2%
    suggested = competitor_price
    action = "⬇️ Decrease"
    rationale = (
        f"Competitor is cheaper ({competitor_price:.0f} SAR). "
        f"Lower our price to match → {suggested:.0f} SAR."
    )

else:
    suggested = our_price
    action = "⏸ No Change"
    rationale = "Prices are equal — no adjustment needed."

# --- Dashboard display ---
st.divider()
st.metric("💡 Action", action)
st.metric("💰 Suggested Price", f"{suggested:.0f} SAR")
st.metric("🏷️ Our Current Price", f"{our_price:.0f} SAR")
st.metric("🏪 Competitor Price", f"{competitor_price:.0f} SAR")

st.info(rationale)
