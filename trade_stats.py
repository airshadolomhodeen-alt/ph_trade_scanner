import pandas as pd

def get_trade_metrics(flow_type):
    """Returns official trade partner rankings and economic zone data sources."""
    if flow_type == "Exports":
        return pd.DataFrame([
            {"Rank": 1, "Partner Country": "United States", "Share (%)": 15.7, "Est. Annual Value (USD B)": 13.44, "Primary PH Export Sectors": "Semiconductors & Electronics", "Data Source": "UN Comtrade / WITS"},
            {"Rank": 2, "Partner Country": "Japan", "Share (%)": 14.0, "Est. Annual Value (USD B)": 11.50, "Primary PH Export Sectors": "Ignition Wiring Sets", "Data Source": "UN Comtrade / PJEPA"},
            {"Rank": 3, "Partner Country": "Hong Kong", "Share (%)": 13.2, "Est. Annual Value (USD B)": 10.80, "Primary PH Export Sectors": "Machinery & Equipment", "Data Source": "UN Comtrade"},
            {"Rank": 4, "Partner Country": "Mainland China", "Share (%)": 11.3, "Est. Annual Value (USD B)": 10.46, "Primary PH Export Sectors": "Processed Foods & Beverages", "Data Source": "UN Comtrade / ASEANStats"},
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
            {"Rank": 2, "Partner Country": "Indonesia", "Share (%)": 8.4, "Est. Annual Value (USD B)": 10.60, "Primary PH Import Sectors": "Mineral Fuels, Coal & Automotive", "Data Source": "ASEANStats"},
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
    return [
        {"Zone Authority": "Bureau of Customs (BOC)", "Official Portal": "https://customs.gov.ph/", "Core Mandate": "Implements CMTA (RA 10863), manages tariff collection, import/export clearance, and FTA Origin Management Systems.", "Key Advantages": "E2M / Value Added Service Providers (VASP) integration, Secure electronic payments."},
        {"Zone Authority": "Tariff Commission (Philippine Tariff Finder)", "Official Portal": "https://finder.tariffcommission.gov.ph/", "Core Mandate": "Houses all 14 Philippine tariff schedules (MFN and 13 FTAs).", "Key Advantages": "Accurate commodity nomenclature classification and tariff lookups."},
        {"Zone Authority": "Philippine Economic Zone Authority (PEZA)", "Official Portal": "https://www.peza.gov.ph/", "Core Mandate": "Promotes investments and public/private ecozones.", "Key Advantages": "Tax holidays (ITH), 5% SCIT under RA 12066."},
        {"Zone Authority": "Subic Bay Freeport Zone (SBMA)", "Official Portal": "https://www.mysubicbay.com.ph/", "Core Mandate": "Manages Subic Bay transshipment and logistics hub.", "Key Advantages": "Duty-free importation of capital equipment."},
        {"Zone Authority": "ASEAN Trade Repository", "Official Portal": "https://data.aseanstats.org/", "Core Mandate": "Official intra-ASEAN trade statistics.", "Key Advantages": "Benchmark for ATIGA compliance."},
        {"Zone Authority": "Labor & Employment Compliance", "Official Portal": "https://www.afablabor.com/", "Core Mandate": "Monitors labor standards across special economic zones.", "Key Advantages": "Workforce compliance guidelines."}
    ]

def get_trade_news_feed():
    return [
        {
            "Headline": "Philippine Exports Extend Growth Streak; Electronics & Coconut Products Drive Strong Inflow",
            "Category": "Export Performance",
            "Date": "September 2026",
            "Source": "DTI / PSA / PortCalls",
            "Summary": "Philippine merchandise exports continue an upward trajectory, led by robust global demand for semiconductors, AI-related components, and coconut-based derivatives."
        },
        {
            "Headline": "Bureau of Customs Deploys FTA Origin Management System (OMS) for Streamlined Preferential Tariffs",
            "Category": "BOC & Tariffs",
            "Date": "September 2026",
            "Source": "BOC (customs.gov.ph)",
            "Summary": "The Bureau of Customs implements CMO rules for online Product Evaluation Reports (PER) and digital Certificate of Origin verifications, drastically lowering compliance turnaround times for traders."
        },
        {
            "Headline": "PEZA Targets ₱300-Billion in New Investments and Expanded Ecozone Developments",
            "Category": "Economic Zones & FDI",
            "Date": "September 2026",
            "Source": "PEZA (peza.gov.ph)",
            "Summary": "The Philippine Economic Zone Authority pushes for export-oriented enterprise registrations, leveraging the enhanced fiscal incentives under the CREATE MORE Act (RA 12066)."
        }
    ]
