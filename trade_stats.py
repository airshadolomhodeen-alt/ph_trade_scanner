import pandas as pd

def get_trade_metrics(flow_type):
    """Returns official trade partner rankings and economic zone data sources."""
    if flow_type == "Exports":
        return pd.DataFrame([
            {"Rank": 1, "Partner Country": "United States", "Share (%)": 15.7, "Est. Annual Value (USD B)": 13.44, "Primary PH Export Sectors": "Semiconductors & Electronics", "Data Source": "UN Comtrade / WITS"},
            {"Rank": 2, "Partner Country": "Japan", "Share (%)": 14.0, "Est. Annual Value (USD B)": 11.50, "Primary PH Export Sectors": "Ignition Wiring Sets", "Data Source": "UN Comtrade / PJEPA"},
            {"Rank": 3, "Partner Country": "Hong Kong", "Share (%)": 13.2, "Est. Annual Value (USD B)": 10.80, "Primary PH Export Sectors": "Machinery & Equipment", "Data Source": "UN Comtrade"},
            {"Rank": 4, "Partner Country": "Mainland China", "Share (%)": 11.3, "Est. Annual Value (USD B)": 10.46, "Primary PH Export Sectors": "Processed Foods & Beverages", "Data Source": "UN Comtrade / ASEANStats (data.aseanstats.org)"},
            {"Rank": 5, "Partner Country": "South Korea", "Share (%)": 4.9, "Est. Annual Value (USD B)": 3.54, "Primary PH Export Sectors": "Coconut Oil & Derivatives", "Data Source": "PKFTA / ASEANStats"},
            {"Rank": 6, "Partner Country": "Singapore", "Share (%)": 4.7, "Est. Annual Value (USD B)": 3.53, "Primary PH Export Sectors": "Copper Metal Products", "Data Source": "ASEANStats"},
            {"Rank": 7, "Partner Country": "Netherlands", "Share (%)": 4.2, "Est. Annual Value (USD B)": 3.60, "Primary PH Export Sectors": "Chemical Products", "Data Source": "ITC Trade Map"},
            {"Rank": 8, "Partner Country": "Thailand", "Share (%)": 4.0, "Est. Annual Value (USD B)": 2.93, "Primary PH Export Sectors": "Apparel & Clothing", "Data Source": "ASEANStats"},
            {"Rank": 9, "Partner Country": "Taiwan", "Share (%)": 3.7, "Est. Annual Value (USD B)": 2.64, "Primary PH Export Sectors": "Ignition Parts", "Data Source": "WITS Database"},
            {"Rank": 10, "Partner Country": "Germany", "Share (%)": 3.4, "Est. Annual Value (USD B)": 2.49, "Primary PH Export Sectors": "Miscellaneous Manufactures", "Data Source": "ITC Trade Map"}
        ])
    else:
        return pd.DataFrame([
            {"Rank": 1, "Partner Country": "Mainland China", "Share (%)": 22.5, "Est. Annual Value (USD B)": 28.50, "Primary PH Import Sectors": "Electronic Components & Raw Materials", "Data Source": "UN Comtrade"},
            {"Rank": 2, "Partner Country": "Indonesia", "Share (%)": 8.4, "Est. Annual Value (USD B)": 10.60, "Primary PH Import Sectors": "Mineral Fuels, Coal & Automotive", "Data Source": "ASEANStats (data.aseanstats.org)"},
            {"Rank": 3, "Partner Country": "Japan", "Share (%)": 7.8, "Est. Annual Value (USD B)": 9.90, "Primary PH Import Sectors": "Machinery & Specialized Equipment", "Data Source": "UN Comtrade / PJEPA"},
            {"Rank": 4, "Partner Country": "United States", "Share (%)": 6.7, "Est. Annual Value (USD B)": 8.50, "Primary PH Import Sectors": "Cereals, Electronics & Capital Goods", "Data Source": "UN Comtrade"},
            {"Rank": 5, "Partner Country": "South Korea", "Share (%)": 6.5, "Est. Annual Value (USD B)": 8.24, "Primary PH Import Sectors": "Semi-conductor Devices & Machinery", "Data Source": "PKFTA"},
            {"Rank": 6, "Partner Country": "Thailand", "Share (%)": 6.2, "Est. Annual Value (USD B)": 7.85, "Primary PH Import Sectors": "Parts of Motor Vehicles & Rice", "Data Source": "ASEANStats"},
            {"Rank": 7, "Partner Country": "Malaysia", "Share (%)": 5.4, "Est. Annual Value (USD B)": 6.84, "Primary PH Import Sectors": "Electrical Machinery & Petroleum", "Data Source": "ASEANStats"},
            {"Rank": 8, "Partner Country": "Taiwan", "Share (%)": 4.8, "Est. Annual Value (USD B)": 6.08, "Primary PH Import Sectors": "Integrated Circuits & Raw Plastics", "Data Source": "WITS Database"},
            {"Rank": 9, "Partner Country": "Singapore", "Share (%)": 3.9, "Est. Annual Value (USD B)": 4.94, "Primary PH Import Sectors": "Mineral Fuels & Chemicals", "Data Source": "ASEANStats"},
            {"Rank": 10, "Partner Country": "Vietnam", "Share (%)": 3.5, "Est. Annual Value (USD B)": 4.43, "Primary PH Import Sectors": "Cereals, Animal Feeds & Electronics", "Data Source": "ASEANStats"}
        ])

def get_economic_zones_directory():
    """Returns official links and key metrics for PEZA, Subic Bay, and Regional Hubs."""
    return [
        {
            "Zone Authority": "Philippine Economic Zone Authority (PEZA)",
            "Official Portal": "https://www.peza.gov.ph/",
            "Core Mandate": "Promotes investments, establishes, and operates public/private ecozones for exporters.",
            "Key Advantages": "Tax holidays (ITH), 5% Special Corporate Income Tax (SCIT), and VAT zero-rating under RA 12066 (CREATE MORE Act)."
        },
        {
            "Zone Authority": "Subic Bay Freeport Zone (SBMA)",
            "Official Portal": "https://www.mysubicbay.com.ph/",
            "Core Mandate": "Manages the Subic Bay Freeport Zone as a premier transshipment and logistics hub.",
            "Key Advantages": "Duty-free and tax-free importation of capital equipment, world-class deep-water port access."
        },
        {
            "Zone Authority": "ASEAN Trade & Statistical Repository",
            "Official Portal": "https://data.aseanstats.org/",
            "Core Mandate": "Official repository for intra-ASEAN trade statistics, harmonization indexes, and tariff schedules.",
            "Key Advantages": "Essential benchmark for ATIGA preferential trade compliance and regional supply chains."
        },
        {
            "Zone Authority": "Regional Labor & Employment Compliance",
            "Official Portal": "https://www.afablabor.com/",
            "Core Mandate": "Monitors labor standards, industrial relations, and workforce compliance across special economic zones.",
            "Key Advantages": "Ensures adherence to Philippine labor codes and fair employment standards for RBEs."
        }
    ]
