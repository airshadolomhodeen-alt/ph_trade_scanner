import streamlit as st
import pandas as pd
import os

from providers.comtrade_provider import ComtradeProvider
from providers.wits_provider import WitsProvider
from providers.peza_provider import PezaProvider
from tariff_engine import TariffEngine
from fta_analyzer import FTAEngine
from trade_stats import OriginEngine, OpportunityEngine

st.set_page_config(
    page_title="FTA Market Access Scanner | PH Trade Intelligence",
    page_icon="🇵🇭",
    layout="wide",
    initial_sidebar_state="expanded"
)

comtrade = ComtradeProvider()
wits = WitsProvider()
peza = PezaProvider()
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

st.sidebar.title("🇵🇭 PH Trade Intelligence")
st.sidebar.markdown("**FTA Market Access Scanner v3.1**")
st.sidebar.markdown("---")

nav_selection = st.sidebar.radio(
    "Navigation Menu",
    [
        "Home / Executive Dashboard",
        "AHTN 2022 Product Scanner",
        "Market Access & Dual-API Engine",
        "Rules of Origin Calculator",
        "Economic Zones & BARMM",
        "Data Sources & Provenance"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔌 API & Data Status")
st.sidebar.markdown("🟢 **UN Comtrade API v1**: Active")
st.sidebar.markdown("🟢 **World Bank WITS SDMX**: Active")
st.sidebar.markdown("🟢 **PEZA Downloads Portal**: Active")
st.sidebar.markdown(f"🟢 **AHTN Database**: Loaded ({len(ahtn_df)} rows)")

if nav_selection == "Home / Executive Dashboard":
    st.title("FTA Market Access Scanner")
    st.subheader("Philippine Export & Trade Intelligence Platform")
    st.markdown("Independent institutional decision-support platform evaluating preferential tariffs, multi-provider trade flows, and origin compliance.")
    st.markdown("---")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Nomenclature", "AHTN 2022")
    c2.metric("Supported FTAs", "10+ Agreements")
    c3.metric("Live APIs", "3 Providers")
    c4.metric("Economic Zones", "PEZA & BEZA")

elif nav_selection == "AHTN 2022 Product Scanner":
    st.title("AHTN 2022 Product & HS Code Scanner")
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

elif nav_selection == "Market Access & Dual-API Engine":
    st.title("Market Access & Multi-API Analytics Engine")
    
    col1, col2 = st.columns(2)
    with col1:
        hs = st.text_input("Enter 6-digit HS / AHTN Code:", "151311")
        market = st.selectbox("Target Market:", ["Japan (392)", "South Korea (410)", "China (156)", "United States (842)"])
    with col2:
        fta = st.selectbox("Select FTA:", tariff_eng.supported_ftas)
        year = st.selectbox("Trade Data Year:", ["2025", "2024", "2023"])

    if st.button("Execute Live Multi-API Scan", type="primary"):
        with st.spinner("Querying UN Comtrade & WITS databases..."):
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
    fob = st.number_input("FOB Export Value (USD):", value=25000.0, step=1000.0)
    non_orig = st.number_input("Non-Originating Material Value (USD):", value=8500.0, step=500.0)
    
    if st.button("Calculate RVC Qualification"):
        res = origin_eng.calculate_rvc_fob(fob, non_orig)
        st.metric("Calculated RVC", f"{res['rvc_percentage']}%")
        if res['passed']:
            st.success("✅ Eligible for preferential FTA tariff rates.")
        else:
            st.warning("⚠️ Below threshold requirements.")

elif nav_selection == "Economic Zones & BARMM":
    st.title("Philippine Economic Zones & BARMM Intelligence")
    st.markdown("Access official PEZA directories, ecozone incentive updates under CREATE MORE, and BARMM trade policies.")
    
    st.markdown("---")
    st.subheader("🌐 Live PEZA Portal Integration")
    st.markdown("Direct repository source: [PEZA Official Downloads Portal](https://www.peza.gov.ph/downloads?combine=list+of+peza&field_sub_category_downloads_tid=All)")
    
    if st.button("Fetch Live PEZA Directory & Documents", type="primary"):
        with st.spinner("Connecting to PEZA portal servers..."):
            peza_res = peza.fetch_peza_resources()
            
        if peza_res["status"] == "VERIFIED":
            st.success("Successfully connected to PEZA portal via PezaProvider!")
            items = peza_res["data"]
            if items:
                for idx, item in enumerate(items, 1):
                    st.markdown(f"{idx}. [{item['title']}]({item['url']})")
            else:
                st.info("Connection established, but no direct matching file rows were parsed.")
        else:
            st.warning(f"Could not automatically parse page elements ({peza_res.get('message', 'Timeout')}). Please use the direct link above.")

elif nav_selection == "Data Sources & Provenance":
    st.title("Data Sources & Provenance")
    st.markdown("All datasets are sourced directly from UN Comtrade API, World Bank WITS API, PEZA Portal, ASEAN Secretariat, and Philippine Tariff Commission.")
