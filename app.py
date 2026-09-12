import streamlit as st
import pandas as pd
from datetime import datetime
from tariff_engine import search_ahtn_database
from fta_analyzer import analyze_market_potential, check_create_more_eligibility, get_ph_fta_database
from trade_stats import get_trade_metrics, get_economic_zones_directory

# --- Page Configuration ---
st.set_page_config(
    page_title="PhilTrade-GIS | PH Trade & Economic Portal", 
    page_icon="🇵🇭", 
    layout="wide"
)

# --- Professional Executive Styling & Theme ---
st.markdown("""
    <style>
    .main {background-color: #F8FAFC;}
    .portal-title {
        font-size: 2.1rem; 
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
    .live-badge {
        background-color: #ECFDF5; 
        color: #065F46; 
        border: 1px solid #A7F3D0;
        padding: 6px 12px; 
        border-radius: 6px; 
        font-size: 0.8rem; 
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    h3 {color: #1E3A8A !important; font-weight: 700 !important;}
    .footer-box {
        background-color: #F1F5F9;
        border: 1px solid #CBD5E1;
        padding: 18px;
        border-radius: 8px;
        font-size: 0.85rem;
        color: #334155;
        margin-top: 40px;
        line-height: 1.6;
    }
    .footer-box a {
        color: #1D4ED8;
        text-decoration: none;
        font-weight: 600;
    }
    .footer-box a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# --- Top Header & Real-Time System Clock ---
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.markdown('<p class="portal-title">🇵🇭 PhilTrade-GIS: Philippine Global Trade & Economic Zone Intelligence Portal</p>', unsafe_allow_html=True)
    st.markdown('<p class="portal-subtitle">Institutional Decision Support System for Exporters, Importers, PEZA Enterprises, and Trade Policy Strategists.</p>', unsafe_allow_html=True)
with col_head2:
    current_time_str = datetime.now().strftime("%B %d, %Y | %H:%M:%S PST")
    st.markdown(f'<div style="text-align: right;"><span class="live-badge">🟢 LIVE SYNC: {current_time_str}</span></div>', unsafe_allow_html=True)

st.markdown("---")

# --- Professional Tab Arrangement ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Macro Trade & Partner Rankings", 
    "🏷️ AHTN Tariff & Product Matrix", 
    "🌍 ITC Market Potential Analyzer", 
    "🌐 International Trade Strategy",
    "🤝 Free Trade Agreements (FTAs)",
    "⚖️ CREATE MORE Act Compliance"
])

with tab1:
    st.subheader("Philippine Bilateral Trade Performance & Partner Rankings")
    st.markdown("Official macroeconomic trade analytics benchmarked against **UN Comtrade, World Bank WITS, and ASEANStats (data.aseanstats.org)**.")
    
    flow_type = st.radio("Select Trade Flow Direction", ["Exports", "Imports"], horizontal=True)
    df_stats = get_trade_metrics(flow_type)
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label=f"Top {flow_type} Partner", value=df_stats.iloc[0]["Partner Country"], delta=f"{df_stats.iloc[0]['Share (%)']}% Share")
    with m2:
        st.metric(label="Tracked Major Markets", value="10 Key Economies", delta="90%+ National Trade Coverage")
    with m3:
        st.metric(label="Primary Sector Focus", value=df_stats.iloc[0]["Primary PH Export Sectors"] if flow_type=="Exports" else df_stats.iloc[0]["Primary PH Import Sectors"])
        
    st.markdown("---")
    st.dataframe(df_stats, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("AHTN-2022 Product Nomenclature & Preferential Tariff Matrix")
    st.markdown("Search across Harmonized System / ASEAN Harmonized Tariff Nomenclature codes to evaluate MFN vs. Preferential FTA rates.")
    
    search_query = st.text_input("Enter HS Code or Keyword (e.g., 'Coconut', 'Semiconductor', 'Banana', '8542')", "Coconut")
    search_results = search_ahtn_database(search_query)
    
    if search_results:
        st.success(f"Matched {len(search_results)} product nomenclature records with embedded tariff intelligence.")
        df_results = pd.DataFrame(search_results)
        st.dataframe(df_results, use_container_width=True, hide_index=True)
    else:
        st.warning(f"No matching product nomenclature found for '{search_query}'. Try broader keywords.")

with tab3:
    st.subheader("Potential Export Market Analyzer (ITC Trade Map Methodology)")
    st.markdown("Evaluate target export destinations using trade gravity models, import demand volume, and preferential tariff advantage margins.")
    
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
            st.info(f"**Strategic Market Classification:** {tier}")

with tab4:
    st.subheader("🌐 International Trade Strategy & Statistical Analytics Hub")
    st.markdown("Advanced policy analytics synthesized from **UN Comtrade, World Bank WITS, ITC Trade Map, and ASEANStats**.")
    
    strategy_tab_choice = st.selectbox("Select Trade Strategy Dimension", [
        "1. Export Diversification & Revealed Comparative Advantage (RCA)",
        "2. Non-Tariff Measures (NTMs) & Sanitary/Phytosanitary (SPS) Compliance",
        "3. Global Value Chain (GVC) Integration & Intermediate Goods Strategy",
        "4. Foreign Direct Investment (FDI) & SEZ Export Competitiveness"
    ])
    
    if "1." in strategy_tab_choice:
        st.markdown("### Export Diversification & Revealed Comparative Advantage (RCA)")
        rca_data = pd.DataFrame({
            "Sector / Product Group": [
                "Electronic Integrated Circuits & Microassemblies (HS 8542)",
                "Electrical Machinery, Equipment & Parts (HS 85)",
                "Fresh Cavendish Bananas & Tropical Fruits (HS 0803)",
                "Coconut (Copra) Oil & Derivatives (HS 1513)",
                "Prepared Tuna & Processed Fish Products (HS 1604)",
                "Ignition Wiring Sets for Vehicles & Aircraft (HS 8544)",
                "Aerospace MRO & Aviation Maintenance Services"
            ],
            "RCA Index Score": [3.85, 2.92, 6.45, 12.10, 4.80, 3.15, 2.40],
            "Global Competitiveness Status": [
                "Strong Comparative Advantage (Top Global Exporter)",
                "High Comparative Advantage",
                "Extreme Specialization (Dominant ASEAN Position)",
                "World-Leading Specialization (Global Copra Leader)",
                "High Comparative Advantage in Processed Food",
                "Strong Integration in Automotive GVCs",
                "Emerging High-Value Service Export"
            ],
            "Primary Destination Markets": [
                "USA, Hong Kong, Singapore, China, Japan",
                "USA, Japan, Germany, Singapore",
                "Japan, South Korea, China, Middle East",
                "USA, Europe (Rotterdam), China",
                "USA, UK, Germany, Japan",
                "Japan, USA, South Korea",
                "North America, Europe, ASEAN"
            ]
        })
        st.dataframe(rca_data, use_container_width=True, hide_index=True)
        st.info("💡 **Strategy Insight:** An RCA index above 1.0 indicates revealed comparative advantage. High RCA scores in coconut oil (12.10) and bananas (6.45) confirm the Philippines is a dominant global supplier.")

    elif "2." in strategy_tab_choice:
        st.markdown("### Non-Tariff Measures (NTMs) & Sanitary/Phytosanitary (SPS) Compliance")
        ntm_data = pd.DataFrame({
            "Target Export Market": ["European Union (EU)", "United States (US FDA)", "China (GACC)", "Japan (MAFF)", "ASEAN Member States"],
            "Primary NTM Constraint": ["Strict Maximum Residue Limits (MRLs) & Traceability", "FSMA Verification, HACCP & Facility Registration", "GACC Decree 248/249 Registration & Quarantine", "Positive List System for Agricultural Chemicals", "ATIGA Certificate of Origin (Form D) Verification"],
            "Compliance Cost Impact": ["High (Requires accredited laboratory testing)", "Moderate-High (Rigorous documentation)", "High (Lengthy clearance procedures)", "Moderate (Strict pesticide residue sampling)", "Low-Moderate (Streamlined digital e-Form D)"],
            "Strategic Mitigation Action": ["Partner with ISO/IEC 17025 accredited testing facilities in PH", "Establish US Agent representation and maintain FDA prior notice compliance", "Secure direct registration via DTI-EMB and Bureau of Customs linkage", "Pre-shipment inspection and residue screening prior to export dispatch", "Leverage ASEAN Single Window (ASW) for paperless trade compliance"]
        })
        st.dataframe(ntm_data, use_container_width=True, hide_index=True)

    elif "3." in strategy_tab_choice:
        st.markdown("### Global Value Chain (GVC) Integration & Intermediate Goods Strategy")
        st.success("""**Strategic Blueprint for GVC Upgrading:**
1. **Backward Integration:** Maximize duty-free importation of high-tech components (semiconductor wafers, raw chemicals) under the **CREATE MORE Act (RA 12066)** via PEZA (peza.gov.ph).
2. **Forward Integration:** Scale up domestic production of specialized auto-wiring harnesses and electronics sub-assemblies.
3. **Digital Supply Chain Transparency:** Implement blockchain and IoT tracking for agricultural exports to meet strict EU/US ESG due diligence regulations.""")

    else:
        st.markdown("### Foreign Direct Investment (FDI) & Special Economic Zone (SEZ) Strategy")
        fdi_data = pd.DataFrame({
            "Strategic Pillar": ["Tax Incentive Structure", "Labor Force Competitiveness", "Infrastructure & Logistics", "Ease of Doing Business"],
            "Philippine Policy Edge (RA 12066)": ["4% to 5% Special Corporate Income Tax (SCIT) or 10-year Corporate Income Tax Holiday (ITH)", "High English proficiency, skilled engineering graduates, young demographic median age (25 years)", "Expanding tollway networks, Clark/Subic/Mactan (mysubicbay.com.ph) gateway integration", "Streamlined one-stop shop registration via PEZA and BOI under CREATE MORE Act"]
        })
        st.dataframe(fdi_data, use_container_width=True, hide_index=True)

with tab5:
    st.subheader("Official Philippine Free Trade Agreements (FTAs) & Preferential Access Matrix")
    st.markdown("Examine active bilateral and regional trade agreements negotiated by the DTI.")
    
    fta_list = get_ph_fta_database()
    df_fta = pd.DataFrame(fta_list)
    st.dataframe(df_fta, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 🔍 Strategic Product & Market Action Plan")
    selected_fta_code = st.selectbox("Select FTA Code to Evaluate Actionable Export Strategy", [fta["FTA Code"] for fta in fta_list])
    
    matched_fta = next((f for f in fta_list if f["FTA Code"] == selected_fta_code), None)
    if matched_fta:
        st.success(f"""**Agreement:** {matched_fta['Agreement Name']}
* **Partner Markets:** {matched_fta['Partner Markets']}
* **High-Priority Product Lines:** {matched_fta['Key Products']}
* **Preferential Tariff Advantage:** {matched_fta['Tariff Advantage']}
* **Strategic Value:** {matched_fta['Strategic Value']}""")

with tab6:
    st.subheader("CREATE MORE Act (RA 12066) Incentives & Compliance Checker")
    st.markdown("Designed for Registered Business Enterprises (RBEs) operating inside PEZA Economic Zones (peza.gov.ph) and Freeports (mysubicbay.com.ph).")
    
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

# --- Official Institutional Portals & References Footer ---
zones_dir = get_economic_zones_directory()
footer_html = """
    <div class="footer-box">
        <strong>🌐 Official Institutional Data Repositories & Economic Zones:</strong><br>
"""
for zone in zones_dir:
    footer_html += f"* 🔗 <strong>{zone['Zone Authority']}:</strong> <a href='{zone['Official Portal']}' target='_blank'>{zone['Official Portal']}</a> — {zone['Core Mandate']}<br>\n"

footer_html += """
        <br><strong>Application Architecture & Development:</strong><br>
        Developed and architected by <strong>Engr. Airsad R. Olomodin, MBA, CBE, PhD</strong>.<br><br>
        <strong>References & Institutional Disclaimer:</strong><br>
        This portal synthesizes official trade datasets benchmarked against <em>UN Comtrade, World Bank World Integrated Trade Solution (WITS), International Trade Centre (ITC) Trade Map, ASEANStats (data.aseanstats.org), PEZA (peza.gov.ph), Subic Bay Freeport (mysubicbay.com.ph), and labor standards (afablabor.com)</em>. Structured for institutional decision support, strategic trade planning, and academic research purposes.
    </div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
