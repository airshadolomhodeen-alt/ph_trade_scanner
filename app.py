import streamlit as st
import pandas as pd
from tariff_engine import search_ahtn_database
from fta_analyzer import analyze_market_potential, check_create_more_eligibility
from trade_stats import get_trade_metrics

st.set_page_config(page_title="PH Economic Zone & Trade Access Scanner", layout="wide")

st.title("🇵🇭 PH Economic Zone & FTA Market Access Scanner")
st.markdown("Advanced Intelligence Portal for PEZA/RBE Enterprises, AEO Importers-Exporters, and Trade Practitioners.")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Macro Trade Stats & Partners", 
    "🏷️ AHTN Search & FTA Matrix", 
    "🌍 Market Potential Analyzer (ITC Style)", 
    "⚖️ CREATE MORE Act (RA 12066) Compliance"
])

with tab1:
    st.header("Top Philippine Export & Import Destinations")
    flow_type = st.radio("Select Trade Flow Direction", ["Exports", "Imports"], horizontal=True)
    df_stats = get_trade_metrics(flow_type)
    st.dataframe(df_stats, use_container_width=True, hide_index=True)

with tab2:
    st.header("AHTN-2022 Product & Tariff Finder (PTF / FTAOMS Style)")
    st.markdown("Search across Philippine MFN and preferential FTA schedules (ATIGA, RCEP, PJEPA, PH-Korea).")
    
    search_query = st.text_input("Enter AHTN Code or Keyword (e.g., '8542.31' or 'Banana')", "8542.31")
    search_results = search_ahtn_database(search_query)
    
    if search_results:
        df_results = pd.DataFrame(search_results)
        df_results.columns = ["AHTN Code", "Description", "MFN (%)", "ATIGA (%)", "RCEP (%)", "PK-FTA (%)", "PJEPA (%)"]
        st.dataframe(df_results, use_container_width=True, hide_index=True)
    else:
        st.warning("No matching product found in the AHTN schedule database.")

with tab3:
    st.header("Potential Market Scanner (ITC Methodology)")
    st.markdown("Evaluate target export destinations using trade gravity models and tariff advantages.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        est_val = st.number_input("Target Market Import Demand (USD M)", value=250.0)
    with col2:
        tariff_adv = st.number_input("Tariff Advantage vs Competitors (%) [MFN minus FTA rate]", value=5.0)
    with col3:
        logistics_val = st.slider("Logistics & Ease Index (0 to 1)", 0.0, 1.0, 0.8)
        
    if st.button("Calculate Market Potential"):
        score, tier = analyze_market_potential(est_val, tariff_adv, logistics_val)
        st.metric(label="Calculated Potential Index Score (/100)", value=score)
        st.info(f"**Market Classification:** {tier}")

with tab4:
    st.header("CREATE MORE Act (RA 12066) Incentives & Compliance Checker")
    st.markdown("Designed for Registered Business Enterprises (RBEs) inside Economic Zones and Freeports.")
    
    is_ree = st.checkbox("Is your enterprise a Registered Export Enterprise (REE)?", value=True)
    export_ratio = st.slider("Actual Export Ratio (% of total annual sales/production)", 0.0, 100.0, 85.0)
    directly_attributable = st.checkbox("Are imported inputs/local purchases directly attributable to registered export activities?", value=True)
    
    if st.button("Verify RA 12066 Incentives Eligibility"):
        passed, log_messages = check_create_more_eligibility(is_ree, export_ratio, directly_attributable)
        for msg in log_messages:
            st.markdown(msg)
            
        if passed:
            st.success("🎉 **Status:** Fully eligible for fiscal incentives, VAT zero-rating on local purchases, and VAT-free importations under the CREATE MORE Act!")
        else:
            st.error("⚠️ **Status:** Review operational thresholds. Failing the 70% export criteria may disqualify enterprise from specific VAT reliefs.")
