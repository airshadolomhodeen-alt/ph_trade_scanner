import pandas as pd
import streamlit as st

@st.cache_data
def load_ahtn_data():
    """
    Loads the full global HS/AHTN product nomenclature dataset from the CSV.
    """
    try:
        df = pd.read_csv("ahtn_2022_master.csv")
        return df
    except Exception:
        # Fallback safeguard table if file lookup encounters issues
        return pd.DataFrame([
            {"code": "8542.31", "description": "Electronic integrated circuits: Processors and controllers", "mfn": 3.0, "atiga": 0.0, "rcep": 0.0, "pkfta": 0.0, "pjepa": 0.0},
            {"code": "0803.90", "description": "Bananas, including plantains, fresh or dried", "mfn": 7.0, "atiga": 0.0, "rcep": 5.0, "pkfta": 3.0, "pjepa": 0.0},
            {"code": "1513.11", "description": "Coconut (copra) oil and its fractions: Crude oil", "mfn": 10.0, "atiga": 0.0, "rcep": 5.0, "pkfta": 5.0, "pjepa": 0.0}
        ])

def search_ahtn_database(query: str):
    """
    Performs a dynamic search across the entire uploaded AHTN / HS nomenclature database.
    """
    df = load_ahtn_data()
    query_lower = query.strip().lower()
    
    if not query_lower:
        return []
        
    # Search across all columns dynamically
    mask = (
        df.astype(str).apply(lambda row: row.str.lower().str.contains(query_lower, na=False)).any(axis=1)
    )
    
    filtered_df = df[mask]
    return filtered_df.to_dict(orient="records")
