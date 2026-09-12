def get_ph_fta_database():
    return [
        {
            "FTA Code": "ATIGA",
            "Agreement Name": "ASEAN Trade in Goods Agreement",
            "Partner Markets": "Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Singapore, Thailand, Vietnam",
            "Key Products": "Electronics, Automotive Parts, Agricultural Goods, Processed Foods",
            "Tariff Advantage": "0% Preferential Duty on 99%+ tariff lines",
            "Strategic Value": "Backbone of regional supply chains and intra-ASEAN sourcing."
        },
        {
            "FTA Code": "ACFTA",
            "Agreement Name": "ASEAN-China Free Trade Area",
            "Partner Markets": "Mainland China & ASEAN Member States",
            "Key Products": "Machinery, Raw Chemical Inputs, Fruits (Bananas, Pineapples), Minerals",
            "Tariff Advantage": "Elimination of tariffs on over 90% of traded goods",
            "Strategic Value": "Primary gateway for intermediate electronics and agricultural export volume."
        },
        {
            "FTA Code": "PJEPA",
            "Agreement Name": "Philippines-Japan Economic Partnership Agreement",
            "Partner Markets": "Japan",
            "Key Products": "Ignition Wiring Sets, Electronic Microassemblies, Fresh Bananas, Tuna",
            "Tariff Advantage": "Duty-free entry for key Philippine agricultural and manufacturing lines",
            "Strategic Value": "Bilateral depth for high-value manufacturing and automotive components."
        },
        {
            "FTA Code": "RCEP",
            "Agreement Name": "Regional Comprehensive Economic Partnership",
            "Partner Markets": "ASEAN + China, Japan, South Korea, Australia, New Zealand",
            "Key Products": "All major industrial sectors, processed agricultural products, services",
            "Tariff Advantage": "Unified Rules of Origin (ROO) and progressive tariff phase-outs",
            "Strategic Value": "Expanded cumulation rules simplifying regional value chain integration."
        },
        {
            "FTA Code": "AKFTA",
            "Agreement Name": "ASEAN-Korea Free Trade Area",
            "Partner Markets": "South Korea & ASEAN",
            "Key Products": "Coconut Oil, Copper Products, Garments, Electronic Parts",
            "Tariff Advantage": "90%+ tariff elimination with sensitive list exceptions",
            "Strategic Value": "Major market access for Philippine oleochemicals and processed food."
        }
    ]

def analyze_market_potential(demand, tariff_adv, logistics):
    score = round((demand * 0.4) + (tariff_adv * 3.5) + (logistics * 25), 1)
    if score >= 75:
        tier = "Tier 1: Prime Target Market (High Demand & High Margin)"
    elif score >= 50:
        tier = "Tier 2: Viable Secondary Market (Moderate Potential)"
    else:
        tier = "Tier 3: Niche or High-Barrier Market"
    return score, tier

def check_create_more_eligibility(is_ree, export_ratio, directly_attributable):
    logs = []
    passed = True
    if not is_ree:
        passed = False
        logs.append("❌ **Disqualification Notice:** Enterprise must be a Registered Export Enterprise (REE) under PEZA or Investment Promotion Agencies (IPAs) to qualify for CREATE MORE Act (RA 12066) incentives.")
    else:
        logs.append("✅ **REE Status Verified:** Enterprise is recognized as a Registered Export Enterprise.")
    
    if export_ratio >= 70.0:
        logs.append(f"✅ **Export Threshold Met:** Export sales ratio is {export_ratio}% (Exceeds the 70% mandatory threshold for REEs).")
    else:
        passed = False
        logs.append(f"❌ **Export Threshold Failed:** Export sales ratio is {export_ratio}%. Must be at least 70% to qualify for full fiscal incentives.")
        
    if directly_attributable:
        logs.append("✅ **VAT Zero-Rating & Duty-Free Compliance:** Local purchases and imported capital equipment/raw materials are directly attributable to registered export activity under RA 12066.")
    else:
        passed = False
        logs.append("❌ **Compliance Error:** Inputs must be directly attributable to export production to enjoy duty-free privileges.")
        
    if passed:
        logs.append("### 🏆 Final Assessment: ELIGIBLE FOR CREATE MORE ACT (RA 12066) INCENTIVES\n* Entitled to **4% to 5% Special Corporate Income Tax (SCIT)** or up to **10-year Corporate Income Tax Holiday (ITH)** plus enhanced deductions.")
    else:
        logs.append("### ⚠️ Final Assessment: ACTION REQUIRED\n* Review operational thresholds before filing with PEZA or BOI.")
    return passed, logs
