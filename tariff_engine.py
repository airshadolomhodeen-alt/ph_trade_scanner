def get_tariff_rates(hs_code, fta_name):
    """Calculates applied MFN tariff vs. preferential FTA tariff."""
    # Base tariff estimation based on code structure
    base_mfn = 15.0 if str(hs_code).startswith("85") or str(hs_code).startswith("84") else 7.5
    
    if "MFN" in fta_name.upper():
        preferential_rate = base_mfn
    else:
        preferential_rate = 0.0 # Most Philippine FTAs reduce tariffs to 0% for qualifying goods
        
    margin = round(base_mfn - preferential_rate, 1)
    
    return {
        "HS Code": hs_code,
        "FTA Agreement": fta_name,
        "MFN Applied Tariff (%)": base_mfn,
        "Preferential FTA Tariff (%)": preferential_rate,
        "Preference Margin (%)": margin,
        "Rules of Origin (RoO)": "Wholly obtained or Substantial Transformation (CTC / RVC 40%)"
    }
