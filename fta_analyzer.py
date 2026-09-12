def analyze_market_potential(export_value_usd_m: float, tariff_advantage: float, logistics_score: float):
    score = (min(export_value_usd_m / 500.0, 1.0) * 40) + (min(tariff_advantage / 15.0, 1.0) * 40) + (logistics_score * 20)
    
    if score >= 75:
        rating = "Tier 1: Prime Export Target (High Unmet Demand & Low Trade Barriers)"
    elif score >= 45:
        rating = "Tier 2: Growth Market (Moderate Potential, Requires Strategic Positioning)"
    else:
        rating = "Tier 3: Niche / High Regulatory Barriers"
        
    return round(score, 2), rating

def check_create_more_eligibility(is_ree: bool, export_ratio: float, directly_attributable: bool):
    messages = []
    qualified = True
    
    if is_ree and export_ratio >= 70.0:
        messages.append("✅ **VAT Zero-Rating on Local Purchases:** Fully qualified under RA 12066 (meets the >= 70% export threshold).")
        messages.append("✅ **VAT-Free Importation:** Capital equipment, raw materials, and spare parts are 100% exempt from import VAT.")
    else:
        qualified = False
        messages.append("❌ **VAT Relief Warning:** Export ratio is below the 70% statutory threshold for registered export enterprises.")
        
    if directly_attributable:
        messages.append("✅ **Enhanced Deductions Regime (EDR):** Eligible for 20% corporate income tax (CIT) rate option and additional deductions (power expense, training, R&D).")
    else:
        messages.append("⚠️ Operating expenses must be directly attributable to registered export production.")
        
    return qualified, messages
