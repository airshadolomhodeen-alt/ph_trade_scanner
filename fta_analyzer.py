def analyze_market_potential(est_val, tariff_adv, logistics_val):
    """Calculates Market Potential Index score based on ITC Trade Map methodology."""
    score = int(min(100, max(0, (est_val / 10.0) + (tariff_adv * 3.0) + (logistics_val * 30.0))))
    if score >= 75:
        tier = "Tier 1: High Priority Export Market (Strong demand & robust preference margins)"
    elif score >= 50:
        tier = "Tier 2: Moderate Opportunity Market (Viable with targeted compliance strategy)"
    else:
        tier = "Tier 3: Niche or High-Barrier Market (Requires strategic cost optimization)"
    return score, tier

def check_create_more_eligibility(is_ree, export_ratio, directly_attributable):
    """Verifies compliance against CREATE MORE Act (RA 12066) provisions."""
    logs = []
    passed_all = True
    
    if is_ree:
        logs.append("✅ **Registered Export Enterprise Status:** Verified under CREATE MORE Act (RA 12066).")
    else:
        logs.append("❌ **Registered Export Enterprise Status:** Must be a certified REE to qualify for export tax privileges.")
        passed_all = False
        
    if export_ratio >= 70.0:
        logs.append(f"✅ **VAT Zero-Rating on Local Purchases:** Fully qualified under RA 12066 (meets the >= 70% export threshold at {export_ratio}%).")
        logs.append("✅ **VAT-Free Importation:** Capital equipment, raw materials, and spare parts are 100% exempt from import VAT.")
        logs.append("✅ **Enhanced Deductions Regime (EDR):** Eligible for 20% corporate income tax (CIT) rate option and additional deductions (power expense, training, R&D).")
    else:
        logs.append(f"⚠️ **Export Threshold Warning:** Current export ratio is {export_ratio}%. RA 12066 requires at least 70% export allocation for full export tax incentives.")
        passed_all = False
        
    if directly_attributable:
        logs.append("✅ **Direct Attributability:** Inputs are directly tied to registered export activity, ensuring full audit compliance.")
    else:
        logs.append("⚠️ **Direct Attributability Warning:** Inputs must be directly attributable to export activity to claim domestic VAT zero-rating.")
        passed_all = False
        
    return passed_all, logs

def get_ph_fta_database():
    """Returns official Free Trade Agreements of the Philippines with active coverage."""
    return [
        {
            "FTA Code": "RCEP",
            "Agreement Name": "Regional Comprehensive Economic Partnership",
            "Partners": "ASEAN (10 member states) + China, Japan, South Korea, Australia, New Zealand",
            "Effective Date": "June 2023",
            "Key Benefits": "Unified rules of origin, expanded market access for electronics, agriculture, and services across 15 major economies."
        },
        {
            "FTA Code": "ATIGA",
            "Agreement Name": "ASEAN Trade in Goods Agreement",
            "Partners": "Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Vietnam",
            "Effective Date": "January 2010",
            "Key Benefits": "0% to 5% preferential tariff rates on intra-ASEAN trade for qualified regional goods."
        },
        {
            "FTA Code": "PJEPA",
            "Agreement Name": "Philippines-Japan Economic Partnership Agreement",
            "Partners": "Japan",
            "Effective Date": "December 2008",
            "Key Benefits": "Bilateral FTA eliminating tariffs on major industrial goods, auto parts, machinery, and key agricultural products (bananas, seafood)."
        },
        {
            "FTA Code": "PKFTA",
            "Agreement Name": "Philippines-Korea Free Trade Agreement",
            "Partners": "South Korea",
            "Effective Date": "December 2024",
            "Key Benefits": "Enhanced market access for Philippine bananas, tropical fruits, and garments in exchange for duty-free or reduced tariffs on Korean autos and components."
        },
        {
            "FTA Code": "PH-EFTA",
            "Agreement Name": "Philippines-European Free Trade Association FTA",
            "Partners": "Iceland, Liechtenstein, Norway, Switzerland",
            "Effective Date": "June 2018",
            "Key Benefits": "Elimination of tariffs on industrial and fisheries exports to high-income European markets outside the EU."
        },
        {
            "FTA Code": "AANZFTA",
            "Agreement Name": "ASEAN-Australia-New Zealand Free Trade Agreement",
            "Partners": "ASEAN + Australia, New Zealand",
            "Effective Date": "January 2010",
            "Key Benefits": "Comprehensive tariff elimination and regional supply chain integration across Oceania and Southeast Asia."
        }
    ]
