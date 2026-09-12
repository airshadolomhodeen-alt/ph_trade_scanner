import streamlit as st
import pandas as pd
from tariff_engine import search_ahtn_database
from fta_analyzer import analyze_market_potential, check_create_more_eligibility
from trade_stats import get_trade_metrics

st.set_page_config(page_title="PH Economic Zone & Global Trade Intelligence Portal", layout="wide")

# --- Custom Styling & Header ---
st.markdown("""
    <style>
    .main-header {font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0px;}
    .sub-header {font-size: 1.0rem; color: #4B5563; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🇵🇭 PH Economic Zone & Global Trade Intelligence Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Advanced Decision Support System for Exporters, Importers, PEZA Enterprises, and Trade Strategists (Integrated with WITS, UN Comtrade, ASEANStats, & ITC Methodologies).</p>', unsafe_allow_html=True)

# --- Professional Navigation Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Macro Bilateral Trade & Partners", 
    "🏷️ AHTN Product Search & Tariff Matrix", 
    "🌍 ITC-Style Market Potential & Trade Map", 
    "🗺️ Philippine Regional Resource Mapping",
    "⚖️ CREATE MORE Act (RA 12066) Compliance"
])

with tab1:
    st.subheader("Philippine Bilateral Trade Performance & Partner Rankings")
    st.markdown("Official trade analytics benchmarked against UN Comtrade and ASEANStats.")
    
    col_a, col_b = st.columns([2, 1])
    with col_a:
        flow_type = st.radio("Select Trade Flow Direction", ["Exports", "Imports"], horizontal=True)
    
    df_stats = get_trade_metrics(flow_type)
    
    # Top metrics summary cards
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label=f"Top {flow_type} Partner", value=df_stats.iloc[0]["Partner Country"], delta=f"{df_stats.iloc[0]['Share (%)']}% Share")
    with m2:
        st.metric(label="Total Tracked Partners", value="10 Major Markets", delta="90%+ Trade Coverage")
    with m3:
        st.metric(label="Primary Sector Focus", value=df_stats.iloc[0]["Primary PH Export Sectors"] if flow_type=="Exports" else df_stats.iloc[0]["Primary PH Import Sectors"])
        
    st.markdown("---")
    st.dataframe(df_stats, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("AHTN-2022 Product & Preferential Tariff Matrix (PTF)")
    st.markdown("Search across 8,244+ WITS nomenclature codes to instantly evaluate **MFN vs. FTA Tariff Savings (ATIGA, RCEP, PH-Korea, PJEPA)**.")
    
    search_query = st.text_input("Enter HS Code or Keyword (e.g., 'Coconut', 'Semiconductor', 'Banana', '8542')", "Coconut")
    search_results = search_ahtn_database(search_query)
    
    if search_results:
        st.success(f"Matched {len(search_results)} product records with embedded trade intelligence.")
        df_results = pd.DataFrame(search_results)
        st.dataframe(df_results, use_container_width=True, hide_index=True)
    else:
        st.warning(f"No matching product found for '{search_query}'. Try broader keywords like 'Oil', 'Fish', or 'Machine'.")

with tab3:
    st.subheader("Potential Export Market Analyzer (ITC Trade Map Methodology)")
    st.markdown("Evaluate target export destinations using trade gravity models, import demand, and preferential tariff advantages.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        est_val = st.number_input("Target Market Import Demand (USD M)", value=350.0)
    with col2:
        tariff_adv = st.number_input("Tariff Advantage vs Competitors (%) [MFN minus FTA rate]", value=5.0)
    with col3:
        logistics_val = st.slider("Logistics & Ease of Trading Index (0 to 1)", 0.0, 1.0, 0.85)
        
    if st.button("Run Market Potential Assessment", type="primary"):
        score, tier = analyze_market_potential(est_val, tariff_adv, logistics_val)
        
        sc1, sc2 = st.columns([1, 2])
        with sc1:
            st.metric(label="Market Potential Index Score", value=f"{score} / 100")
        with sc2:
            st.info(f"**Strategic Classification:** {tier}")
            
        st.markdown("---")
        st.markdown("### Actionable Recommendations for Importer-Exporter:")
        st.markdown("* **Certificate of Origin (CO):** Apply for Form D (ATIGA) or RCEP CO to capture 0% preferential tariffs.")
        st.markdown("* **Logistics Routing:** Leverage direct shipping lanes from Manila/Cebu to target port hubs.")

with tab4:
    st.subheader("Philippine Regional Resource & Industry Cluster Mapping")
    st.markdown("Align your export product lines with regional raw material strengths and investment promotion agencies (PEZA, BOI).")
    
    region_choice = st.selectbox("Select Philippine Region / Economic Hub", [
        "CALABARZON (Region IV-A) - Electronics & Automotive",
        "Davao Region (Region XI) - Agribusiness (Bananas, Coconuts, Fruit)",
        "Central Visayas (Region VII / Mactan PEZA) - Aerospace & Electronics",
        "Northern Mindanao (Region X) - Coconuts, Steel & Agro-Industrial",
        "National Capital Region (NCR) - Global Services & Trading HQs"
    ])
    
    if "CALABARZON" in region_choice:
        st.success("**Key Sectors:** Semiconductor assembly, automotive wiring, electrical machinery.\n\n**Investment Agencies:** PEZA, BOI\n\n**Major Economic Zones:** Laguna Technopark, Gateway Business Park, Lima Technology Center.")
    elif "Davao" in region_choice:
        st.success("**Key Sectors:** Cavendish bananas, fresh pineapples, coconut products, cacao.\n\n**Investment Agencies:** MinDA, BOI, DTI-XI\n\n**Export Destinations:** Japan, China, Middle East, South Korea.")
    elif "Visayas" in region_choice:
        st.success("**Key Sectors:** MRO aerospace parts, electronics manufacturing, furniture, tourism tech.\n\n**Investment Agencies:** Mactan Export Processing Zone (MEPZ), Cebu CFI.\n\n**Export Destinations:** USA, EU, Japan.")
    elif "Mindanao" in region_choice:
        st.success("**Key Sectors:** Crude coconut oil, copra cake, steel manufacturing, processed fruit.\n\n**Investment Agencies:** PHividec Industrial Estate, BOI.\n\n**Export Destinations:** Europe, USA, ASEAN neighbors.")
    else:
        st.success("**Key Sectors:** Headquarters, Logistics, BPO/IT, International Trading Hubs.\n\n**Investment Agencies:** DTI-FIEB, BOI.\n\n**Scope:** National and international trade brokerage.")

with tab5:
    st.subheader("CREATE MORE Act (RA 12066) Incentives & Compliance Checker")
    st.markdown("Designed for Registered Business Enterprises (RBEs) operating inside PEZA Economic Zones and Freeports.")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        is_ree = st.checkbox("Is your enterprise a Registered Export Enterprise (REE)?", value=True)
        export_ratio = st.slider("Actual Export Ratio (% of total annual production/sales)", 0.0, 100.0, 85.0)
    with col_c2:
        directly_attributable = st.checkbox("Are imported raw materials and local purchases directly attributable to export activity?", value=True)
    
    if st.button("Verify RA 12066 Eligibility", type="primary"):
        passed, log_messages = check_create_more_eligibility(is_ree, export_ratio, directly_attributable)
        for msg in log_messages:
            st.markdown(msg)
            
        if passed:
            st.success("🎉 **Status:** Fully compliant! Eligible for 0% VAT on local purchases, VAT-free importations, and the Enhanced Deductions Regime under RA 12066.")
        else:
            st.error("⚠️ **Status:** Threshold review required. Failing the 70% export requirement may subject transactions to standard VAT rules.")
