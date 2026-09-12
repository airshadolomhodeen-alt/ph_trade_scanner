import pandas as pd
import streamlit as st

@st.cache_data
def load_ahtn_data():
    """
    Safely loads the WITS/HS master nomenclature CSV using latin1 encoding.
    """
    try:
        df = pd.read_csv("ahtn_2022_master.csv", encoding='latin1', on_bad_lines='skip')
        # Clean up column names
        df.columns = [str(c).strip() for c in df.columns]
        return df
    except Exception as e:
        # Fallback if any error occurs
        return pd.DataFrame(columns=["ProductCode", "Product Description", "Tier"])

def search_ahtn_database(query: str):
    """
    Searches across all columns of the 8,000+ product WITS master database.
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
