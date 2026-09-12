import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from tariff_engine import search_ahtn_database
from fta_analyzer import analyze_market_potential, check_create_more_eligibility, get_ph_fta_database
from trade_stats import get_trade_metrics

st.set_page_config(page_title="PH Economic Zone & Global Trade Intelligence Portal", layout="wide")

# --- Custom Styling & Real-Time Header ---
st.markdown("""
    <style>
    .main-header {font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0px;}
    .sub-header {font-size: 1.0rem; color: #4B5563; margin-bottom: 10px;}
    .live-badge {background-color: #DEF7EC; color: #03543F; padding: 4px 10px; border-radius: 6px; font-size: 0.85rem; font-weight: 600;}
    </style>
""", unsafe_allow_html=True)

col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.markdown('<p class="main-header">🇵🇭 PH Economic Zone & Global Trade Intelligence Portal</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Advanced Decision Support System for Exporters, Importers, PEZA Enterprises, and Trade Strategists.</p>', unsafe_allow_html=True)
with col_head2:
    current_time_str = datetime.now().strftime("%B %d, %Y | %H:%M:%S PST")
    st.markdown(f'<br><span class="live-badge">🟢 LIVE SYNC: {current_time_str}</span>', unsafe_allow_html=True)

st.markdown("---")

# Define all 6 professional tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Macro Bilateral Trade & Partners", 
    "🏷️ AHTN Product Search & Tariff Matrix", 
    "🌍 ITC-Style Market Potential & Trade Map", 
    "🗺️ Philippine Regional & Interactive Map Hub",
    "⚖️ CREATE MORE Act (RA 12066) Compliance",
    "🤝 Philippine Free Trade Agreements (FTAs)"
])

with tab1:
    st.subheader("Philippine Bilateral Trade Performance & Partner Rankings")
    st.markdown("Official trade analytics benchmarked against UN Comtrade, WITS, and ASEANStats.")
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
    st.markdown("Search across 8,244+ nomenclature codes to evaluate MFN vs. FTA Tariff Savings (ATIGA, RCEP, PH-Korea, PJEPA).")
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

with tab4:
    st.subheader("Philippine Regional Resource & Interactive Map Hub")
    st.markdown("Explore key regional production clusters, PEZA economic hubs, and special freeports across the Philippines.")
    
    # Interactive Map Data Frame with real Philippine coordinates
    map_data = pd.DataFrame({
        'lat': [14.5995, 13.4125, 7.1907, 10.3157, 8.4542, 6.9214, 15.1450, 16.0433],
        'lon': [120.9842, 121.2000, 125.4553, 123.8854, 124.6319, 122.0790, 120.5887, 120.3333],
        'Hub Name': [
            "NCR - National Trading & Logistics HQ", 
            "CALABARZON - Laguna Technopark & Automotive Hub", 
            "Davao Region - Agribusiness & Banana/Cacao Export Center", 
            "Central Visayas - Mactan PEZA Aerospace & Electronics Hub", 
            "Northern Mindanao - PHividec Industrial & Steel Hub", 
            "Zamboanga Peninsula - Sardine & Halal Processing Center",
            "Central Luzon - Clark Freeport & Logistics Zone",
            "Ilocos Region - Renewable Energy & Mango Export Hub"
        ]
    })
    
    st.map(map_data, zoom=5, use_container_width=True)
    st.caption("📍 Interactive map displaying key Philippine economic zones and export processing hubs.")
    
    st.markdown("---")
    region_choice = st.selectbox("Select Region / Economic Hub for Detailed Intelligence", [
        "BARMM (Bangsamoro Autonomous Region) - Halal Agribusiness, Fisheries, Seaweeds & Corn",
        "CALABARZON (Region IV-A) - Electronics, Automotive & Heavy Industries",
        "Davao Region (Region XI) - Agribusiness (Bananas, Coconuts, Cacao, Fruit)",
        "Central Visayas (Region VII / Mactan PEZA) - Aerospace MRO, Electronics & Furniture",
        "Northern Mindanao (Region X) - Coconuts, Steel, Agro-Industrial & Logistics",
        "National Capital Region (NCR) - Global Services, Logistics & Trading HQs"
    ])
    
    if "BARMM" in region_choice:
        st.success("""**Key Sectors & Resources:** 
* Halal-certified processed foods, agricultural produce, and ingredients
* High-grade carrageenan (seaweed farming - major global exporter)
* Yellow corn, Robusta coffee, and tropical fruits

**Investment & Trade Agencies:** 
* **Bangsamoro Economic Zone Authority (BEZA-BARMM)** – Establishes and regulates special economic zones and freeports.
* **Bangsamoro Board of Investments (BBOI)** & **Ministry of Trade, Investments and Tourism (MTIT-BARMM)**.

**Export Advantage:** Strategic participation in the **BIMP-EAGA** growth area and expanding Halal-compliant trade channels across MENA and Southeast Asia.""")
    else:
        st.success(f"**Selected Hub Profile:** {region_choice}\n\n**Strategic Focus:** Regional commodity integration, PEZA/BOI tax incentive alignment, and international export supply chain logistics.")

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

with tab6:
    st.subheader("Official Philippine Free Trade Agreements (FTAs) & Preferential Access")
    st.markdown("Examine active bilateral and regional trade agreements negotiated by the DTI to eliminate tariff barriers.")
    
    fta_list = get_ph_fta_database()
    st.dataframe(pd.DataFrame(fta_list), use_container_width=True, hide_index=True)
