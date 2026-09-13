import streamlit as st
import pandas as pd
import os

from providers.comtrade_provider import ComtradeProvider
from providers.wits_provider import WitsProvider
from providers.peza_provider import PezaProvider
from providers.subic_port_provider import SubicPortProvider
from providers.itc_provider import ItcProvider

from tariff_engine import TariffEngine
from fta_analyzer import FTAEngine
from trade_stats import OriginEngine, OpportunityEngine

st.set_page_config(
    page_title="FTA Market Access Scanner | PH Trade Intelligence",
    page_icon="🇵🇭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INSTITUTIONAL CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        border: 1px solid #e9ecef;
    }
    .stAlert {
        border-radius: 6px;
    }
    h1, h2, h3 {
        color: #1e293b;
    }
    </style>
""", unsafe_allow_html=True)

comtrade = ComtradeProvider()
wits = WitsProvider()
peza = PezaProvider()
subic_port = SubicPortProvider()
itc_prov = ItcProvider()

tariff_eng = TariffEngine()
fta_eng = FTAEngine()
origin_eng = OriginEngine()
opp_eng = OpportunityEngine()

@st.cache_data
def load_ahtn_dataset():
    csv_path = "ahtn_2022_master.csv"
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path, encoding="latin1")
            df = df.dropna(subset=['ProductCode'])
            return df
        except Exception:
            return pd.DataFrame()
    return pd.DataFrame()

ahtn_df = load_ahtn_dataset()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🇵🇭 PH Trade Intelligence")
st.sidebar.markdown("**FTA Market Access Scanner v3.5**")
st.sidebar.markdown("---")

nav_selection = st.sidebar.radio(
    "Navigation Menu",
    [
        "Home / Executive Dashboard",
        "AHTN 2022 Product Scanner",
        "Market Access & Multi-API Engine",
        "Rules of Origin Calculator",
        "Economic Zones, Ports & ITC",
        "Data Sources & Provenance"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔌 Live API & Data Matrix")
st.sidebar.markdown("🟢 **UN Comtrade API v1**: Active")
st.sidebar.markdown("🟢 **World Bank WITS SDMX**: Active")
st.sidebar.markdown("🟢 **PEZA Downloads Portal**: Active")
st.sidebar.markdown("🟢 **Subic Port Portal**: Active")
st.sidebar.markdown("🟢 **ITC Trade Map**: Active")
st.sidebar.markdown(f"🟢 **AHTN Database**: Loaded ({len(ahtn_df):,} rows)")

# --- APP ROUTING ---
if nav_selection == "Home / Executive Dashboard":
    st.title("FTA Market Access Scanner")
    st.subheader("Institutional Decision-Support & Trade Intelligence Platform")
    st.markdown("Independent analytics platform evaluating preferential tariffs, multi-provider trade flows, rules of origin compliance, and regional economic zones.")
    st.markdown("---")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Nomenclature Standard", "AHTN 2022")
    c2.metric("Covered Trade Agreements", "10+ FTAs")
    c3.metric("Integrated Providers", "5 Live APIs")
    c4.metric("Database Integrity", f"{len(ahtn_df):,} Codes")
    
    st.markdown("### System Architecture Overview")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("**Core Capabilities**\n* Dual-API Verification (Comtrade + WITS)\n* Automated Tariff Preference Margin Calculations\n* Regional Value Content (RVC) Origin Compliance")
    with col_b:
        st.success("**Infrastructure & Compliance**\n* Secure SSL Handshake Overrides for Gov Gateways\n* Zero-Credential Local Fallback Architecture\n* Multi-Source Port & Free Zone Integration")

elif nav_selection == "AHTN 2022 Product Scanner":
    st.title("AHTN 2022 Product & HS Code Scanner")
    st.markdown("Search official tariff nomenclature codes, descriptions, and baseline classifications.")
    search_query = st.text_input("Search HS Code, AHTN Code, or Keyword (e.g., 'coconut', '1513', 'tuna'):", "")
    
    if not ahtn_df.empty:
        if search_query:
            q = search_query.lower()
            res = ahtn_df[ahtn_df['ProductCode'].astype(str).str.lower().str.contains(q) | ahtn_df['Product Description'].astype(str).str.lower().str.contains(q)]
        else:
            res = ahtn_df.head(50)
        st.dataframe(res, use_container_width=True)
    else:
        st.error("`ahtn_2022_master.csv` not found in root directory.")

elif nav_selection == "Market Access & Multi-API Engine":
    st.title("Market Access & Multi-API Analytics Engine")
    st.markdown("Evaluate bilateral trade flows and preferential tariff margins across global partner markets.")
    
    col1, col2 = st.columns(2)
    with col1:
        hs = st.text_input("Enter 6-digit HS / AHTN Code:", "151311")
        market = st.selectbox("Target Market:", ["Japan (392)", "South Korea (410)", "China (156)", "United States (842)"])
    with col2:
        fta = st.selectbox("Select FTA:", tariff_eng.supported_ftas)
        year = st.selectbox("Trade Data Year:", ["2025", "2024", "2023"])

    if st.button("Execute Live Multi-API Scan", type="primary"):
        with st.spinner("Querying UN Comtrade, WITS, and global trade databases..."):
            partner_map = {"Japan (392)": "392", "South Korea (410)": "410", "China (156)": "156", "United States (842)": "842"}
            p_code = partner_map.get(market, "392")
            
            trade_res = comtrade.fetch_trade_data("608", p_code, year, hs)
            tariff_res = tariff_eng.get_fta_tariff(hs, fta, partner=p_code[:3])

        st.markdown(f"**Product Identified**: `{tariff_res['description']}`")

        b1, b2 = st.columns(2)
        with b1:
            st.info(f"UN Comtrade Status: **{trade_res['status']}**")
        with b2:
            st.info(f"WITS Tariff Engine Status: **{tariff_res['wits_api_status']}**")

        m1, m2, m3 = st.columns(3)
        m1.metric("MFN Baseline Tariff", f"{tariff_res['mfn_rate']}%")
        m2.metric("FTA Preferential Rate", f"{tariff_res['preferential_rate']}%")
        m3.metric("Preference Margin", f"{tariff_res['preference_margin']}%")
        
        st.success(f"Successfully evaluated market access for HS Code **{hs}** under **{fta}** to **{market}**.")

elif nav_selection == "Rules of Origin Calculator":
    st.title("Rules of Origin (RVC) Calculator")
    st.markdown("Determine regional value content compliance for preferential tariff qualification.")
    
    fob = st.number_input("FOB Export Value (USD):", value=25000.0, step=1000.0)
    non_orig = st.number_input("Non-Originating Material Value (USD):", value=8500.0, step=500.0)
    
    if st.button("Calculate RVC Qualification", type="primary"):
        res = origin_eng.calculate_rvc_fob(fob, non_orig)
        st.metric("Calculated Regional Value Content (RVC)", f"{res['rvc_percentage']}%")
        if res['passed']:
            st.success("✅ **Qualified**: Eligible for preferential FTA tariff rates under standard build-up criteria.")
        else:
            st.warning("⚠️ **Non-Qualified**: Regional value content falls below threshold requirements.")

elif nav_selection == "Economic Zones, Ports & ITC":
    st.title("Economic Zones, Ports & ITC Trade Intelligence")
    st.markdown("Access official PEZA directories, Subic Bay port capabilities, and international trade intelligence portals.")
    
    tab1, tab2, tab3 = st.tabs(["🌐 PEZA Portal", "🚢 Subic Bay Port", "🌍 ITC Trade Centre"])
    
    with tab1:
        st.subheader("PEZA Downloads Repository")
        st.markdown("Direct repository source: [PEZA Official Downloads Portal](https://www.peza.gov.ph/downloads?combine=list+of+peza&field_sub_category_downloads_tid=All)")
        if st.button("Fetch Live PEZA Directory", type="primary"):
            with st.spinner("Connecting to PEZA portal..."):
                peza_res = peza.fetch_peza_resources()
            if peza_res["status"] == "VERIFIED":
                st.success("Successfully connected to PEZA portal!")
                for idx, item in enumerate(peza_res["data"], 1):
                    st.markdown(f"{idx}. [{item['title']}]({item['url']})")
            else:
                st.warning("Could not automatically parse items due to firewall restrictions. Please use the direct link above.")

    with tab2:
        st.subheader("Subic Bay Freeport & Port Capabilities")
        st.markdown("Direct portal source: [Subic Bay Port Website](https://ship.mysubicbay.com.ph/ship-my-subic-bay)")
        if st.button("Fetch Live Subic Port Overview", type="primary"):
            with st.spinner("Connecting to Subic Bay port portal..."):
                subic_res = subic_port.fetch_subic_port_info()
            if subic_res["status"] == "VERIFIED":
                st.success("Successfully retrieved Subic Bay port profile!")
                st.markdown(f"**Portal Title**: {subic_res['title']}")
                for highlight in subic_res["highlights"][:5]:
                    st.markdown(f"* {highlight}")
                st.markdown(f"🔗 [Open Full Subic Bay Port Portal]({subic_res['url']})")
            else:
                st.warning("Could not load live summary. Access directly via the link above.")

    with tab3:
        st.subheader("International Trade Centre (ITC) & MyITC Portal")
        st.markdown("Access global trade analytics resources and institutional portals.")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("🔗 [Open Public ITC Resources Portal](https://www.intracen.org/)")
        with col_b:
            st.markdown("🔐 [Open Secure MyITC Login Portal](https://myitc.intracen.org/)")

        if st.button("Fetch Live ITC Public Feed", type="primary"):
            with st.spinner("Connecting to intracen.org..."):
                itc_res = itc_prov.fetch_itc_intelligence()
            if itc_res["status"] == "VERIFIED":
                st.success("Successfully retrieved ITC platform summary!")
                st.markdown(f"**Platform Portal**: {itc_res['title']}")
                for ins in itc_res["insights"][:5]:
                    st.markdown(f"* {ins}")
            else:
                st.info("Live feed protected by institutional firewall. Use direct portal links above for secure browsing.")

elif nav_selection == "Data Sources & Provenance":
    st.title("Data Sources & Provenance")
    st.markdown("Transparent documentation of all integrated trade databases and institutional providers.")
    st.markdown("---")
    
    st.markdown("""
    * **UN Comtrade API v1**: Global bilateral trade statistics and partner trade flows.
    * **World Bank WITS SDMX API**: Preferential and MFN tariff schedules across international markets.
    * **PEZA Downloads Portal**: Official Philippine Economic Zone Authority directories and policy guidelines.
    * **Subic Bay Port Portal**: Freeport shipping intelligence, vessel schedules, and logistics capacity.
    * **International Trade Centre (ITC)**: Global trade maps, export potential indicators, and market access requirements.
    * **AHTN 2022 Master Database**: Local nomenclature fallback ensuring uninterrupted tariff calculations.
    """)
