import streamlit as st
import pandas as pd
import os

# Import functions from your root-level Python modules
from trade_stats import get_top_ph_trading_partners
from tariff_engine import get_tariff_rates
from fta_analyzer import calculate_global_demand_and_supply, get_top_competitors

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="FTA Market Access Scanner | Phil. Trade Intelligence",
    page_icon="🇵🇭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LOAD AHTN DATASET CACHE ---
@st.cache_data
def load_ahtn_data():
    csv_path = "ahtn_2022_master.csv"
    if os.path.exists(csv_path):
        try:
            return pd.read_csv(csv_path, encoding="latin-1")
        except Exception:
            return pd.DataFrame()
    return pd.DataFrame()

df_ahtn = load_ahtn_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🇵🇭 FTA Market Access Scanner")
st.sidebar.markdown("**Philippine Export & Trade Intelligence**")
st.sidebar.divider()

nav_page = st.sidebar.radio(
    "Navigation Menu",
    [
        "Home & Executive Overview", 
        "Product Scanner (AHTN)", 
        "Market Access & Demand Engine", 
        "Top 20 Trade Partners Dashboard", 
        "Economic Zones & BARMM", 
        "About & Data Sources"
    ]
)

# --- PAGE 1: HOME & EXECUTIVE OVERVIEW ---
if nav_page == "Home & Executive Overview":
    st.title("🇵🇭 Philippine Export & Trade Intelligence Platform")
    st.markdown("### *Empowering Exporters, Trade Policymakers, and Investors with Actionable Data-Driven Insights*")
    
    st.divider()
    
    st.subheader("📌 Executive Summary: Why This Platform Matters")
    st.markdown("""
    Navigating international trade requires answering critical strategic questions before committing capital or shipping goods. This platform bridges the information gap by synthesizing complex customs nomenclature (AHTN), Preferential Tariffs under Philippine Free Trade Agreements (FTAs), Rules of Origin, and global trade flows into a unified decision-support engine. 
    
    Specifically, this platform is engineered to resolve four pillars of modern trade intelligence:
    1. **Where is global demand highest?** By analyzing global import trends and partner consumption indices, exporters can instantly pinpoint high-growth destination countries for specific product lines.
    2. **Who are the top 20 trading partners of the Philippines?** Providing a granular breakdown of major bilateral trade flows, export volumes, and persistent trade deficits or surpluses.
    3. **How are trade balances, supply, and demand calculated?** Using econometric gravity models combined with verified UN Comtrade and PSA baseline data to compute apparent consumption, market gaps, and national comparative advantages.
    4. **How do we diagnose specific export products and competitive positioning?** By cross-referencing AHTN codes against MFN vs. FTA preferential tariffs, calculating preference margins, and evaluating dominant competitor nations in target markets.
    """)
    
    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Philippine FTAs", "12 Agreements", "RCEP, ATIGA, AJCEPA, etc.")
    col2.metric("Tracked Trading Partners", "Top 20 Nations", "Covering >85% of Total Trade")
    col3.metric("Nomenclature Database", "AHTN 2022 Standard", f"{len(df_ahtn)} Records Loaded")

# --- PAGE 2: PRODUCT SCANNER (AHTN) ---
elif nav_page == "Product Scanner (AHTN)":
    st.title("🔍 AHTN 2022 Product Code Scanner")
    st.markdown("Search through official AHTN product classifications to identify exact headings, chapters, and descriptions.")
    
    search_query = st.text_input("Enter product keyword or HS/AHTN code (e.g., 'coconut', '1513', 'electronics')", "1513")
    
    if not df_ahtn.empty:
        mask = df_ahtn.astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
        filtered_df = df_ahtn[mask]
        
        st.write(f"Found **{len(filtered_df)}** matching records for query: `{search_query}`")
        st.dataframe(filtered_df.head(100), use_container_width=True)
    else:
        st.warning("AHTN master dataset (`ahtn_2022_master.csv`) not found or empty in working directory.")
        sample_data = [
            {"NomenclatureCode": "AHTN 2022", "ProductCode": "151311", "Product Description": "Crude coconut (copra) oil"},
            {"NomenclatureCode": "AHTN 2022", "ProductCode": "080390", "Product Description": "Fresh or dried bananas"},
            {"NomenclatureCode": "AHTN 2022", "ProductCode": "854231", "Product Description": "Electronic integrated circuits as processors and controllers"}
        ]
        st.dataframe(pd.DataFrame(sample_data), use_container_width=True)

# --- PAGE 3: MARKET ACCESS & DEMAND ENGINE ---
elif nav_page == "Market Access & Demand Engine":
    st.title("🌐 Market Access, Demand & Supply Engine")
    st.markdown("Evaluate target market import demand, preference margins, and competitor supply for any Philippine export product.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        hs_input = st.text_input("HS / AHTN Code", "1513.11")
    with c2:
        market_input = st.selectbox("Target Export Market", ["United States", "Japan", "China", "South Korea", "Germany", "Singapore", "Australia", "Thailand"])
    with c3:
        fta_input = st.selectbox("Applicable FTA", ["RCEP", "ATIGA (ASEAN)", "AJCEPA (Japan)", "AKFTA (Korea)", "PH-EFTA", "MFN (No FTA)"])
        
    if st.button("Run Market Access & Demand Analysis"):
        metrics = calculate_global_demand_and_supply(hs_input, market_input)
        tariff_info = get_tariff_rates(hs_input, fta_input)
        competitors = get_top_competitors(hs_input, market_input)
        
        st.success(f"Analysis Complete for HS Code `{hs_input}` in `{market_input}` via `{fta_input}`")
        
        col_a, col_b, col_c, col_d = st.columns(4)
        col_a.metric("Total Import Demand", f"${metrics['Total Import Demand (USD M)']:,} M")
        col_b.metric("PH Export Value", f"${metrics['PH Export Value (USD M)']:,} M")
        col_c.metric("Preference Margin", f"{tariff_info['Preference Margin (%)']}%")
        col_d.metric("Opportunity Score", f"{metrics['Market Opportunity Score']} / 100")
        
        st.divider()
        st.subheader("📋 Tariff & Rules of Origin Analysis")
        st.json(tariff_info)
        
        st.subheader("📊 Competitor Supply Analysis in Target Market")
        st.dataframe(competitors, use_container_width=True)

# --- PAGE 4: TOP 20 TRADE PARTNERS DASHBOARD ---
elif nav_page == "Top 20 Trade Partners Dashboard":
    st.title("📊 Top 20 Philippine Trading Partners Dashboard")
    st.markdown("Empirical overview of the top 20 bilateral trade partners, total trade values, export/import shares, and trade balances.")
    
    partners_df = pd.DataFrame(get_top_ph_trading_partners())
    st.dataframe(partners_df, use_container_width=True)
    
    st.info("💡 **Trade Balance Insight:** The Philippines typically maintains a trade deficit with raw material and fuel suppliers like China, Indonesia, and South Korea, while securing robust trade surpluses with export destinations like the United States, Hong Kong, and Japan.")

# --- PAGE 5: ECONOMIC ZONES & BARMM ---
elif nav_page == "Economic Zones & BARMM":
    st.title("🏭 Philippine Economic Zones & BARMM Intelligence")
    st.markdown("Analyze strategic investment locations, fiscal incentives under the CREATE MORE Act, and regional supply chain integration in BARMM.")
    
    tab1, tab2 = st.tabs(["PEZA / Economic Zones", "BARMM Export Gateway"])
    
    with tab1:
        st.subheader("Key Investment Promotion Agencies (IPAs)")
        ez_data = [
            {"Zone / Authority": "PEZA (Philippine Economic Zone Authority)", "Focus": "Manufacturing, IT-BPM, Electronics Export", "Incentives": "Income Tax Holiday (ITH) + Enhanced Deductions"},
            {"Zone / Authority": "SBMA (Subic Bay Metropolitan Authority)", "Focus": "Maritime logistics, heavy industry, warehousing", "Incentives": "Duty-free importation of capital equipment"},
            {"Zone / Authority": "CDC (Clark Development Corporation)", "Focus": "Aviation, high-tech manufacturing, logistics", "Incentives": "Special corporate tax rate & tax exemptions"}
        ]
        st.dataframe(pd.DataFrame(ez_data), use_container_width=True)
        
    with tab2:
        st.subheader("Bangsamoro Autonomous Region in Muslim Mindanao (BARMM) Potential")
        barmm_data = [
            {"Sector": "Coconut & Coconut Oil", "Current Status": "High primary production", "Export Potential": "High value-added oleochemicals"},
            {"Sector": "Halal Food Processing", "Current Status": "Growing ecosystem", "Export Potential": "Global Halal markets in ASEAN & Middle East"},
            {"Sector": "Seaweed & Fisheries (Tuna)", "Current Status": "Major regional contributor", "Export Potential": "Cold-chain processing and direct export"}
        ]
        st.dataframe(pd.DataFrame(barmm_data), use_container_width=True)

# --- PAGE 6: ABOUT & DATA SOURCES ---
elif nav_page == "About & Data Sources":
    st.title("ℹ️ About the Platform & Data Sources")
    st.markdown("""
    **FTA Market Access Scanner & Philippine Trade Intelligence Platform**  
    *An independent decision-support tool designed for exporters, investors, and trade economists.*
    
    ### Authoritative Data Sources Referenced:
    * **Philippine Statistics Authority (PSA):** National merchandise trade performance and partner statistics.
    * **Department of Trade and Industry (DTI):** FTA schedules, Rules of Origin, and export promotion frameworks.
    * **UN Comtrade & WITS:** International import demand, competitor market shares, and bilateral trade matrices.
    * **Tariff Commission:** AHTN nomenclature and MFN applied tariff schedules.
    
    **Architect / Developer:** Engr. Airsad R. Olomodin, MBA, CBE, PhD  
    """)
