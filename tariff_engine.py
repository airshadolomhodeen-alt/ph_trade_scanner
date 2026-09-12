import pandas as pd
import streamlit as st

@st.cache_data
def load_ahtn_data():
    try:
        df = pd.read_csv("ahtn_2022_master.csv", encoding='latin1', on_bad_lines='skip')
        df.columns = [str(c).strip() for c in df.columns]
        return df
    except Exception:
        return pd.DataFrame(columns=["ProductCode", "Product Description", "Tier"])

def get_product_intelligence(product_code: str, description: str):
    """
    Simulates elite trade intelligence (ITC Trade Map & WITS style) for any selected product code.
    Provides MFN tariffs, FTA rates (ATIGA, RCEP, PH-Korea, PJEPA), top global buyers, and PH resource alignment.
    """
    code_str = str(product_code).strip()
    desc_lower = str(description).lower()
    
    # Intelligent baseline estimation based on HS chapters
    if code_str.startswith("08") or "coconut" in desc_lower or "banana" in desc_lower or "fruit" in desc_lower:
        mfn, atiga, rcep, pkfta, pjepa = 7.0, 0.0, 3.0, 3.0, 0.0
        top_buyers = ["United States", "China", "Japan", "South Korea", "Netherlands"]
        ph_hub = "Davao Region, Southern Mindanao, Quezon Province"
        export_demand = "High Global Demand (Growing at 6.4% CAGR)"
    elif code_str.startswith("85") or "electronic" in desc_lower or "circuit" in desc_lower or "semi-conductor" in desc_lower:
        mfn, atiga, rcep, pkfta, pjepa = 1.0, 0.0, 0.0, 0.0, 0.0
        top_buyers = ["Hong Kong", "United States", "China", "Singapore", "Japan"]
        ph_hub = "CALABARZON (Laguna, Cavite), Mactan Economic Zone (Cebu)"
        export_demand = "Very High Global Demand (Core PH Export Driver)"
    elif code_str.startswith("15") or "oil" in desc_lower:
        mfn, atiga, rcep, pkfta, pjepa = 10.0, 0.0, 5.0, 5.0, 0.0
        top_buyers = ["China", "Netherlands", "United States", "Malaysia", "South Korea"]
        ph_hub = "Northern Mindanao, Southern Tagalog"
        export_demand = "Stable Global Demand with High Value-Add Potential"
    else:
        mfn, atiga, rcep, pkfta, pjepa = 5.0, 0.0, 2.0, 3.0, 0.0
        top_buyers = ["United States", "Japan", "China", "Singapore", "Germany"]
        ph_hub = "Nationwide PEZA Economic Zones & Freeports"
        export_demand = "Moderate-to-High Market Potential"
        
    return {
        "MFN Rate (%)": mfn,
        "ATIGA (ASEAN) (%)": atiga,
        "RCEP (%)": rcep,
        "PH-Korea FTA (%)": pkfta,
        "PJEPA (Japan) (%)": pjepa,
        "Top Global Import Markets": ", ".join(top_buyers),
        "PH Regional Production Hubs": ph_hub,
        "Market Assessment": export_demand
    }

def search_ahtn_database(query: str):
    df = load_ahtn_data()
    query_lower = query.strip().lower()
    
    if not query_lower:
        return []
        
    mask = (
        df.astype(str).apply(lambda row: row.str.lower().str.contains(query_lower, na=False)).any(axis=1)
    )
    
    filtered_df = df[mask].head(25) # Limit to top 25 matches for UI clarity
    records = filtered_df.to_dict(orient="records")
    
    # Enrich records with trade intelligence indicators
    enriched = []
    for rec in records:
        p_code = rec.get("ProductCode", "N/A")
        p_desc = rec.get("Product Description", "N/A")
        intel = get_product_intelligence(p_code, p_desc)
        
        combined = {**rec, **intel}
        enriched.append(combined)
        
    return enriched
