import streamlit as st
import pandas as pd
from tariff_engine import search_ahtn_database
from fta_analyzer import analyze_market_potential, check_create_more_eligibility
from trade_stats import get_trade_metrics

st.set_page_config(page_title="PH Economic Zone & Global Trade Intelligence Portal", layout="wide")

st.markdown("""
    <style>
    .main-header {font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0px;}
    .sub-header {font-size: 1.0rem; color: #4B5563; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🇵🇭 PH Economic Zone & Global Trade Intelligence Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Advanced Decision Support System for Exporters, Importers, PEZA Enterprises, and Trade Strategists (Integrated with WITS, UN Comtrade, ASEANStats, & ITC Methodologies).</p>', unsafe_allow_html=True)

# Define all 5 tabs upfront
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
    flow_type = st.radio("Select Trade Flow Direction", ["Exports", "Imports"], horizontal=True)
    df_stats = get_trade_metrics(flow_type)
    
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
    st.markdown("Search across 8,244+ WITS nomenclature codes to evaluate MFN vs. FTA Tariff Savings.")
    search_query = st.text_input("Enter HS Code or Keyword (e.g., 'Coconut', 'Semiconductor', 'Banana', '8542')", "Coconut")
    search_results = search_ahtn_database(search_query)
    
    if search_results:
        st.success(f"Matched {len(search_results)} product records with embedded trade intelligence.")
        df_results = pd.DataFrame(search_results)
        st.dataframe(df_results, use_container_width=True, hide_index=True)
    else:
        st.warning(f"No matching product found for '{search_query}'. Try broader keywords.")

with tab3:
    st.subheader("Potential Export Market Analyzer (ITC Trade Map Methodology)")
    st.markdown("Evaluate target export destinations using trade gravity models and tariff advantages.")
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

with tab4:
    st.subheader("Philippine Regional Resource & Industry Cluster Mapping")
    st.markdown("Align your export product lines with regional raw material strengths, Halal trade potential, and investment promotion agencies (PEZA, BOI, BEZA-BARMM).")
    
    region_choice = st.selectbox("Select Philippine Region / Economic Hub", [
        "BARMM (Bangsamoro Autonomous Region) - Halal Agribusiness, Fisheries, Seaweeds & Corn",
        "CALABARZON (Region IV-A) - Electronics, Automotive & Heavy Industries",
        "Davao Region (Region XI) - Agribusiness (Bananas, Coconuts, Cacao, Fruit)",
        "Central Visayas (Region VII / Mactan PEZA) - Aerospace MRO, Electronics & Furniture",
        "Northern Mindanao (Region X) - Coconuts, Steel, Agro-Industrial & Logistics",
        "National Capital Region (NCR) - Global Services, Logistics & Trading HQs",
        "Ilocos Region (Region I) - Mangoes, Tobacco, Renewable Energy & IT-BPM",
        "Cagayan Valley (Region II) - Corn, Legumes, Coffee & High-Value Crops",
        "Central Luzon (Region III / Clark-Subic) - Aviation, Logistics, Electronics & Agribusiness",
        "Western Visayas (Region VI) - Sugar, Renewable Energy, Aqua-marine & Tourism Tech",
        "Eastern Visayas (Region VIII) - Geothermal Energy, Coconut Products & Minerals",
        "Zamboanga Peninsula (Region IX) - Sardines, Rubber, Coconut & Halal Trade",
        "SOCCSKSARGEN (Region XII) - Tuna Capital, Pineapple, Coffee & Palm Oil",
        "Caraga (Region XIII) - Timber, Mining, Aqua-culture & Nickel Processing"
    ])
    
    if "BARMM" in region_choice:
        st.success("""**Key Sectors & Resources:** 
* Halal-certified processed foods, agricultural produce, and ingredients
* High-grade carrageenan (seaweed farming - major global exporter)
* Yellow corn, Robusta coffee, and tropical fruits
* Artisanal fisheries, aquaculture, and cold-chain logistics

**Investment & Trade Agencies:** 
* **Bangsamoro Economic Zone Authority (BEZA-BARMM)** – Establishes and regulates special economic zones, offering fiscal and non-fiscal incentives.
* **Bangsamoro Board of Investments (BBOI)** and **Ministry of Trade, Investments and Tourism (MTIT-BARMM)**.

**Export Advantages & Markets:** Strategic participation in the **BIMP-EAGA (Brunei-Indonesia-Malaysia-Philippines East ASEAN Growth Area)** and expanding Halal-compliant trade channels across the Middle East, North Africa (MENA), and Southeast Asia.""")
    else:
        st.success(f"**Selected Hub:** {region_choice}\n\n**Strategic Focus:** Regional commodity integration, domestic distribution, and value-chain processing for international export compliance.")

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
