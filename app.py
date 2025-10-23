if competitor_price > our_price:
    suggested = competitor_price * (1 - discount_margin)
    action = "⬆️ Increase"
    rationale = f"Competitor is selling higher ({competitor_price:.0f} SAR). Raise price to stay 2% below → {suggested:.0f} SAR."
elif competitor_price < our_price:
    suggested = competitor_price
    action = "⬇️ Decrease"
    rationale = f"Competitor is cheaper ({competitor_price:.0f} SAR). Match their price → {suggested:.0f} SAR."
else:
    suggested = our_price
    action = "⚖️ Maintain"
    rationale = "Price matches competitor."
