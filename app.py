import streamlit as st
from tariff_engine import lookup_tariff
from fta_analyzer import check_roo_eligibility
from trade_stats import get_trade_metrics

st.set_page_config(page_title="PH Trade & FTA Scanner", layout="wide")

st.title("🇵🇭 International Trade & FTA Market Access Scanner")
st.markdown("Scan global markets, query live international trade parameters, and evaluate preferential tariff frameworks.")

tab1, tab2, tab3 = st.tabs(["📊 Trade Stats & Top Partners", "🏷️ Tariff & MFN Engine", "📜 Rules of Origin (RoO) Checker"])

with tab1:
    st.header("Top Philippine Export & Import Destinations")
    flow_type = st.radio("Trade Direction", ["Exports", "Imports"], horizontal=True)
    df_stats = get_trade_metrics(flow_type)
    st.dataframe(df_stats, use_container_width=True, hide_index=True)

with tab2:
    st.header("AHTN-2022 Tariff & FTA Matrix Lookup")
    col1, col2 = st.columns(2)
    with col1:
        hs_code = st.text_input("AHTN Code", "8542.31")
    with col2:
        partner = st.selectbox("Trading Partner / Agreement", ["China", "Japan", "South Korea", "ASEAN", "Global (MFN)"])
        
    if st.button("Run Tariff Analysis"):
        res = lookup_tariff(hs_code, partner)
        st.success(f"Applicable Rate: **{res['rate']}%** under **{res['regime']}**")
        st.caption(res['notes'])

with tab3:
    st.header("FTA Rules of Origin Qualification Screener")
    fta = st.selectbox("Agreement Type", ["RCEP", "ATIGA", "PH-Korea (PKFTA)"])
    rvc = st.slider("Regional Value Content (RVC %)", 0, 100, 40)
    ctc_changed = st.checkbox("Change in Tariff Classification (CTC) criteria satisfied?")
    
    if st.button("Evaluate Eligibility"):
        eligible, reason = check_roo_eligibility(fta, rvc, ctc_changed)
        if eligible:
            st.success(f"✅ Qualified for Preferential Access under {fta}. Reason: {reason}")
        else:
            st.warning(f"❌ Qualification Failed. Reason: {reason}")
