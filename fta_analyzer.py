def analyze_market_potential(export_value_usd_m: float, tariff_advantage: float, logistics_score: float):
    """
    Calculates Market Potential Index based on ITC methodology.
    """
    score = (min(export_value_usd_m / 500.0, 1.0) * 40) + (min(tariff_advantage / 15.0, 1.0) * 40) + (logistics_score * 20)
    
    if score >= 75:
        rating = "Tier 1: Prime Export Target (High Potential)"
    elif score >= 45:
        rating = "Tier 2: Growth Market (Moderate Potential)"
    else:
        rating = "Tier 3: Niche / High Barriers"
        
    return round(score, 2), rating

def check_create_more_eligibility(is_ree: bool, export_ratio: float, directly_attributable: bool):
    """
    Evaluates compliance incentives under the CREATE MORE Act (RA 12066).
    """
    messages = []
    qualified = True
    
    if is_ree and export_ratio >= 70.0:
        messages.append("✅ **VAT Zero-Rating on Local Purchases:** Qualified under RA 12066 (meets >= 70% export threshold).")
        messages.append("✅ **VAT-Free Importation:** Capital equipment and raw materials are exempt from import VAT if directly attributable.")
    else:
        qualified = False
        messages.append("❌ **VAT Relief Warning:** Export ratio is below 70%. Standard tax rules apply.")
        
    if directly_attributable:
        messages.append("✅ **Enhanced Deductions Regime (EDR):** Eligible for 20% CIT rate option and specialized deductions (power, training, R&D).")
    else:
        messages.append("⚠️ Expenses must be directly attributable to registered export activities to qualify for EDR bonuses.")
        
    return qualified, messages
