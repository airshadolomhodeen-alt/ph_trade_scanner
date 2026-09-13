import os
import pandas as pd

def search_ahtn_database(query):
    """
    Searches the AHTN-2022 master database CSV file with robust fallback 
    and data freshness provenance labeling.
    """
    csv_filename = "ahtn_2022_master.csv"
    
    if os.path.exists(csv_filename):
        try:
            df = pd.read_csv(csv_filename)
            query_lower = query.lower()
            filtered = df[
                df.astype(str).apply(lambda row: row.str.lower().str.contains(query_lower).any(), axis=1)
            ]
            if not filtered.empty:
                results = filtered.to_dict(orient="records")
                for r in results:
                    r["Data Status"] = "VERIFIED (AHTN-2022 Master)"
                return results
        except Exception:
            pass

    # Fallback dataset with clear provenance
    fallback_data = [
        {"HS Code": "1513.11", "Description": "Crude coconut (copra) oil and its fractions", "MFN Rate (%)": "10%", "ATIGA (ASEAN) Rate (%)": "0%", "RCEP Rate (%)": "0%", "Data Status": "INDICATIVE / MODEL ESTIMATE", "Key Compliance / Notes": "Export leader; requires FDA / PCA clearance"},
        {"HS Code": "0803.90", "Description": "Fresh or dried bananas (including Cavendish)", "MFN Rate (%)": "30%", "ATIGA (ASEAN) Rate (%)": "0%", "RCEP Rate (%)": "0%", "Data Status": "INDICATIVE / MODEL ESTIMATE", "Key Compliance / Notes": "SPS clearance from Bureau of Plant Industry (BPI)"},
        {"HS Code": "8542.31", "Description": "Electronic integrated circuits as processors and controllers", "MFN Rate (%)": "0%", "ATIGA (ASEAN) Rate (%)": "0%", "RCEP Rate (%)": "0%", "Data Status": "INDICATIVE / MODEL ESTIMATE", "Key Compliance / Notes": "PEZA / Zone Enterprise duty-free raw material entry"}
    ]
    
    query_lower = query.lower()
    matched = [
        item for item in fallback_data 
        if query_lower in item["HS Code"].lower() or query_lower in item["Description"].lower()
    ]
    return matched if matched else fallback_data
