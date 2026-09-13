def analyze_market_potential(est_val, tariff_adv, logistics_val):
    """Calculates an export market potential index score based on gravity model metrics."""
    score = (est_val * 0.05) + (tariff_adv * 3.5) + (logistics_val * 40.0)
    score = min(max(round(score, 1), 12.5), 98.5)
    
    if score >= 75:
        tier = "Tier 1: High Priority Export Growth Market"
    elif score >= 50:
        tier = "Tier 2: Moderate Potential Market"
    else:
        tier = "Tier 3: Niche / Emerging Market"
        
    return score, tier

def check_create_more_eligibility(is_ree, export_ratio, directly_attributable):
    """Validates enterprise tax and duty incentive eligibility under the CREATE MORE Act (RA 12066)."""
    logs = []
    passed = True
    
    if is_ree:
        logs.append("✅ **REE Status:** Confirmed under RA 12066.")
    else:
        passed = False
        logs.append("❌ **REE Status:** Non-compliant. Must hold REE registration.")
        
    if export_ratio >= 70.0:
        logs.append(f"✅ **Export Ratio ({export_ratio}%):** Meets statutory threshold (>70%).")
    else:
        passed = False
        logs.append(f"❌ **Export Ratio ({export_ratio}%):** Below mandatory 70% threshold.")
        
    if directly_attributable:
        logs.append("✅ **Direct Input Criterion:** Verified for VAT zero-rating.")
    else:
        passed = False
        logs.append("❌ **Direct Input Criterion:** Unverified.")
        
    return passed, logs

def get_ph_fta_database():
    """Returns the complete inventory of Philippine Free Trade Agreements formatted for screen fit."""
    return [
        {
            "Code": "ATIGA",
            "Agreement Name": "ASEAN Trade in Goods Agreement",
            "Partners": "ASEAN (10 Member States)",
            "Status": "ACTIVE",
            "Tariff Concession": "0% across ~99% tariff lines",
            "Provenance": "DTI-EMB / ASEAN Repository"
        },
        {
            "Code": "RCEP",
            "Agreement Name": "Regional Comprehensive Econ. Partnership",
            "Partners": "ASEAN, CN, JP, KR, AU, NZ",
            "Status": "ACTIVE",
            "Tariff Concession": "Phased elimination schedules",
            "Provenance": "Tariff Commission"
        },
        {
            "Code": "PH-KR",
            "Agreement Name": "Philippines–Korea Free Trade Agreement",
            "Partners": "Philippines, South Korea",
            "Status": "ACTIVE",
            "Tariff Concession": "Elimination of duties on agri/industrial",
            "Provenance": "DTI / EO 80"
        },
        {
            "Code": "PJEPA",
            "Agreement Name": "PH-Japan Economic Partnership Agreement",
            "Partners": "Philippines, Japan",
            "Status": "ACTIVE",
            "Tariff Concession": "Bilateral tariff eliminations (>90%)",
            "Provenance": "DTI-EMB"
        },
        {
            "Code": "PH-EFTA",
            "Agreement Name": "PH–European Free Trade Association FTA",
            "Partners": "CH, NO, IS, LI",
            "Status": "ACTIVE",
            "Tariff Concession": "Duty-free industrial/fisheries",
            "Provenance": "DTI-EMB"
        },
        {
            "Code": "ACFTA",
            "Agreement Name": "ASEAN–China Free Trade Area",
            "Partners": "ASEAN, China",
            "Status": "ACTIVE",
            "Tariff Concession": "Normal Track 0% tariff",
            "Provenance": "Tariff Commission"
        },
        {
            "Code": "AKFTA",
            "Agreement Name": "ASEAN–Korea Free Trade Area",
            "Partners": "ASEAN, South Korea",
            "Status": "ACTIVE",
            "Tariff Concession": "Progressive tariff reduction",
            "Provenance": "DTI-EMB"
        },
        {
            "Code": "AANZFTA",
            "Agreement Name": "ASEAN–Australia–New Zealand FTA",
            "Partners": "ASEAN, Australia, New Zealand",
            "Status": "ACTIVE",
            "Tariff Concession": "Comprehensive elimination (>90%)",
            "Provenance": "Tariff Commission"
        },
        {
            "Code": "AIFTA",
            "Agreement Name": "ASEAN–India Free Trade Area",
            "Partners": "ASEAN, India",
            "Status": "ACTIVE",
            "Tariff Concession": "Gradual tariff concessions",
            "Provenance": "DTI-EMB"
        },
        {
            "Code": "AJCEPA",
            "Agreement Name": "ASEAN–Japan Comprehensive Partnership",
            "Partners": "ASEAN, Japan",
            "Status": "ACTIVE",
            "Tariff Concession": "Regional tariff reductions",
            "Provenance": "Tariff Commission"
        },
        {
            "Code": "AHKFTA",
            "Agreement Name": "ASEAN–Hong Kong, China FTA",
            "Partners": "ASEAN, Hong Kong SAR",
            "Status": "ACTIVE",
            "Tariff Concession": "Preferential commitments",
            "Provenance": "DTI-EMB"
        }
    ]
