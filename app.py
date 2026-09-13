import streamlit as st
import pandas as pd
from datetime import datetime
from tariff_engine import search_ahtn_database
from fta_analyzer import analyze_market_potential, check_create_more_eligibility, get_ph_fta_database

# --- Page Configuration ---
st.set_page_config(
    page_title="FTA Market Access Scanner | Philippine Trade Intelligence", 
    page_icon="🇵🇭", 
    layout="wide"
)

# --- Professional Institutional Styling ---
st.markdown("""
    <style>
    .main {background-color: #F8FAFC;}
    .portal-title {
        font-size: 1.9rem; 
        font-weight: 800; 
        color: #0F172A; 
        letter-spacing: -0.5px;
        margin-bottom: 0px;
    }
    .portal-subtitle {
        font-size: 0.95rem; 
        color: #475569; 
        font-weight: 500;
        margin-top: 4px;
        margin-bottom: 15px;
    }
    .provenance-badge {
        background-color: #FEF3C7; 
        color: #92400E; 
        border: 1px solid #FCD34D;
        padding: 4px 10px; 
        border-radius: 4px; 
        font-size: 0.75rem; 
        font-weight: 600;
        display: inline-block;
    }
    .verified-badge {
        background-color: #ECFDF5; 
        color: #065F46; 
        border: 1px solid #A7F3D0;
        padding: 4px 10px; 
        border-radius: 4px; 
        font-size: 0.75rem; 
        font-weight: 600;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header & Provenance Banner ---
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.markdown('<p class="portal-title">🇵🇭 FTA Market Access Scanner</p>', unsafe_allow_html=True)
    st.markdown('<p class="portal-subtitle">Philippine Export & Trade Intelligence Platform | Decision Support System</p>', unsafe_allow_html=True)
with col_head2:
    st.markdown('<div style="text-align: right;"><span class="verified-badge">🟢 STATUS: ACTIVE ENGINE</span></div>', unsafe_allow_html=True)

st.markdown("---")

# --- Structured Multi-Tab Navigation ---
tab_home, tab_scanner, tab_market_access, tab_fta, tab_origin, tab_economic_zones, tab_sources = st.tabs([
    "🏠 Home / Overview", 
    "🔍 Product Scanner", 
    "📊 Market Access Snapshot", 
    "🌐 FTA Database", 
    "⚖️ Rules of Origin (ROO)", 
    "🏛️ Economic Zones & CREATE MORE", 
    "📚 Data Sources & Provenance"
])

with tab_home:
    st.subheader("Find the Best Market for Your Philippine Product")
    st.markdown("Analyze FTA market access, tariffs, Rules of Origin, trade demand, and Philippine economic-zone advantages.")
    
    col_w1, col_w2, col_w3 = st.columns(3)
    with col_w1:
        st.info("**1. Select Product & HS Code**\n\nSearch across AHTN-2022 nomenclature for verified product classifications.")
    with col_w2:
        st.info("**2. Evaluate Market & FTAs**\n\nCompare MFN versus preferential FTA tariff rates and preference margins.")
    with col_w3:
        st.info("**3. Assess Origin & Incentives**\n\nReview Rules of Origin criteria and PEZA / CREATE MORE Act (RA 12066) incentives.")

with tab_scanner:
    st.subheader("AHTN-2022 Product Nomenclature & Tariff Scanner")
    search_query = st.text_input("Enter HS Code or Keyword (e.g., 'Coconut', 'Bananas', '8542')", "Coconut")
    results = search_ahtn_database(search_query)
    if results:
        st.success(f"Matched {len(results)} nomenclature records.")
        st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)
    else:
        st.warning("DATA CURRENTLY UNAVAILABLE for this query.")

with tab_market_access:
    st.subheader("Market Access Opportunity & Gravity Assessment")
    c1, c2, c3 = st.columns(3)
    with c1:
        demand = st.number_input("Target Market Import Demand (USD M)", value=250.0)
    with c2:
        adv = st.number_input("Tariff Preference Margin (%) [MFN minus FTA]", value=5.0)
    with c3:
        log = st.slider("Logistics Index (0 to 1)", 0.0, 1.0, 0.8)
        
    if st.button("Calculate Opportunity Score", type="primary"):
        score, tier = analyze_market_potential(demand, adv, log)
        st.metric(label="FTA Market Access Opportunity Score", value=f"{score} / 100")
        st.info(f"**Classification:** {tier}")

with tab_fta:
    st.subheader("Structured Philippine Free Trade Agreements (FTAs)")
    st.markdown("Verified preferential trade agreements maintained by the DTI and Tariff Commission.")
    fta_db = get_ph_fta_database()
    st.dataframe(pd.DataFrame(fta_db), use_container_width=True, hide_index=True)

with tab_origin:
    st.subheader("Rules of Origin (ROO) & Origin Assessment Engine")
    st.markdown("Determine whether your export product potentially qualifies for preferential tariff treatment.")
    st.markdown("> **Note:** Products are classified as **POTENTIALLY ELIGIBLE** pending submission of a formal Product Evaluation Report (PER) and supporting documentation.")
    
    col_o1, col_o2 = st.columns(2)
    with col_o1:
        fob = st.number_input("FOB Export Value (USD)", value=10000.0)
        non_orig = st.number_input("Non-Originating Material Cost (USD)", value=3000.0)
    with col_o2:
        rvc = ((fob - non_orig) / fob) * 100
        st.metric(label="Calculated Regional Value Content (RVC)", value=f"{rvc:.1f}%")
        if rvc >= 40.0:
            st.success("✅ **Status:** POTENTIALLY ELIGIBLE (Exceeds standard 40% RVC threshold).")
        else:
            st.warning("⚠️ **Status:** INSUFFICIENT RVC (Below 40% threshold).")

with tab_economic_zones:
    st.subheader("Economic Zones & CREATE MORE Act (RA 12066) Compliance")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        is_ree = st.checkbox("Is your enterprise a Registered Export Enterprise (REE)?", value=True)
        ratio = st.slider("Export Ratio (%)", 0.0, 100.0, 80.0)
    with col_e2:
        attr = st.checkbox("Directly attributable to export activity?", value=True)
        
    if st.button("Verify RA 12066 Eligibility"):
        passed, logs = check_create_more_eligibility(is_ree, ratio, attr)
        for l in logs:
            st.markdown(l)

with tab_sources:
    st.subheader("Data Sources, Provenance & Legal Disclaimer")
    st.markdown("""
    * **Primary Sources:** DTI Export Marketing Bureau, Tariff Commission Philippine Tariff Finder, Bureau of Customs (BOC), UN Comtrade, ASEANstats.
    * **Data Freshness Classification:** <span class="verified-badge">VERIFIED DATA</span> | <span class="provenance-badge">INDICATIVE / MODEL ESTIMATE</span>
    
    > **Legal Disclaimer:** This platform provides independent trade intelligence and decision-support analysis. It is not an official government customs, tariff classification, or FTA certification system.
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("**Application Architecture:** Developed by Engr. Airsad R. Olomodin, MBA, CBE, PhD")
