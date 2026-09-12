import pandas as pd
import streamlit as st

def get_trade_metrics(flow_type: str):
    if flow_type == "Exports":
        data = {
            "Rank": list(range(1, 11)),
            "Partner Country": ["United States", "Japan", "Hong Kong", "Mainland China", "South Korea", "Singapore", "Netherlands", "Thailand", "Taiwan", "Germany"],
            "Share (%)": [15.7, 14.0, 13.2, 11.3, 4.9, 4.7, 4.2, 4.0, 3.7, 3.4],
            "Est. Annual Value (USD B)": [13.44, 11.50, 10.80, 10.46, 3.54, 3.53, 3.60, 2.93, 2.64, 2.49],
            "Primary PH Export Sectors": [
                "Semiconductors & Electronics", "Ignition Wiring Sets", "Machinery & Equipment", 
                "Processed Foods & Beverages", "Coconut Oil & Derivatives", "Copper Metal Products", 
                "Chemical Products", "Apparel & Clothing", "Ignition Parts", "Miscellaneous Manufactures"
            ]
        }
    else:
        data = {
            "Rank": list(range(1, 11)),
            "Partner Country": ["Mainland China", "Indonesia", "Japan", "South Korea", "United States", "Singapore", "Thailand", "Malaysia", "Vietnam", "Taiwan"],
            "Share (%)": [28.4, 7.5, 7.3, 7.0, 6.5, 5.8, 5.2, 4.6, 4.1, 3.8],
            "Est. Annual Value (USD B)": [38.22, 10.16, 10.52, 12.70, 9.69, 8.46, 7.65, 6.68, 4.77, 5.10],
            "Primary PH Import Sectors": [
                "Electronic Components", "Mineral Fuels & Petroleum", "Iron, Steel & Metals", 
                "Cereals & Industrial Machinery", "Plastics & Polymers", "Organic Chemicals", 
                "Transport Equipment", "Optical & Medical Instruments", "Dairy Products", "Paper & Paperboard"
            ]
        }
    return pd.DataFrame(data)
