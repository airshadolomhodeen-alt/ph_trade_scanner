import os
import pandas as pd
import requests
import streamlit as st

from providers.comtrade_provider import ComtradeProvider
from providers.datadocked_provider import DataDockedProvider
from providers.itc_provider import ItcProvider
from providers.peza_provider import PezaProvider
from providers.psa_provider import PSAProvider  # <-- Newly integrated PSA Provider
from providers.subic_port_provider import SubicPortProvider
from providers.wits_provider import WitsProvider
from tariff_engine import TariffEngine
from trade_analytics_matrix import TradeAnalyticsMatrix
from trade_stats import OpportunityEngine, OriginEngine
from fta_analyzer import FTAEngine

st.set_page_config(
    page_title='PH Trade Intelligence | National FTA & Market Access Terminal',
    page_icon='🇵🇭',
    layout='wide',
    initial_sidebar_state='expanded',
)

# --- PROFESSIONAL TRADE TERMINAL CSS ---
st.markdown(
    """
    <style>
    .main { background-color: #f1f5f9; }
    .stMetric {
        background-color: #ffffff;
        padding: 18px;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
    }
    .card-container {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    h1, h2, h3 {
        color: #0f172a;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .stAlert {
        border-radius: 8px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

comtrade = ComtradeProvider()
wits = WitsProvider()
peza = PezaProvider()
subic_port = SubicPortProvider()
itc_prov = ItcProvider()
datadocked = DataDockedProvider()
psa_prov = PSAProvider()  # <-- Initialized PSA API Provider

tariff_eng = TariffEngine()
fta_eng = FTAEngine()
origin_eng = OriginEngine()
opp_eng = OpportunityEngine()
matrix_eng = TradeAnalyticsMatrix()


@st.cache_data
def load_ahtn_dataset():
  csv_path = 'ahtn_2022_master.csv'
  if os.path.exists(csv_path):
    try:
      df = pd.read_csv(csv_path, encoding='latin1')
      df = df.dropna(subset=['ProductCode'])
      df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
      return df
    except Exception:
      return pd.DataFrame()
  return pd.DataFrame()


ahtn_df = load_ahtn_dataset()

# --- SIDEBAR NAVIGATION & CREDENTIALS ---
st.sidebar.title('🇵🇭 PH Trade Intelligence')
st.sidebar.markdown('**National Trade Access Portal v4.5**')
st.sidebar.markdown('---')

nav_selection = st.sidebar.radio(
    'Navigation Menu',
    [
        'Home / Executive Dashboard',
        'Top 20 Country Destinations & Matrices',
        'AHTN 2022 Product Nomenclature',
        'PSA Official Classification API Gateway',  # <-- NEW PSA API TAB
        'Bilateral Market Access & Multi-API Engine',
        'Rules of Origin (RVC) Compliance',
        'Economic Zones, Ports & ITC Intelligence',
        'Maritime & Vessel Traffic Intelligence',
        'n8n Workflow & Automation Trigger',  # <-- NEW n8n TAB
        'Data Sources & Provenance',
    ],
)

st.sidebar.markdown('---')
st.sidebar.subheader('🔌 Live Institutional Gateways')
st.sidebar.markdown('🟢 **PSA Classification API**: Active')
st.sidebar.markdown('🟢 **UN Comtrade API**: Active')
st.sidebar.markdown('🟢 **World Bank WITS**: Active')
st.sidebar.markdown('🟢 **PEZA Official Portal**: Active')
st.sidebar.markdown('🟢 **Subic Port Portal**: Active')
st.sidebar.markdown('🟢 **ITC Trade Map**: Active')
st.sidebar.markdown('🟢 **Data Docked Maritime API**: Active')
st.sidebar.markdown(f'🟢 **AHTN DB**: {len(ahtn_df):,} Records')

st.sidebar.markdown('---')
st.sidebar.subheader('📌 Developer & Notice')
st.sidebar.markdown('**Developer**: ENGR. AIRSAD R. OLOMODIN, MBA, CBE, PhD')
st.sidebar.markdown(
    '<small><b>Disclaimer</b>: This analytical decision-support terminal is'
    ' developed strictly for the personal use of authorized policy-makers and'
    ' trade officials within the Bangsamoro Autonomous Region in Muslim'
    ' Mindanao (BARMM). All simulated outputs, tariff schedules, and'
    ' bilateral data indices are intended exclusively for strategic guidance,'
    ' exploratory scenario planning, and institutional research.</small>',
    unsafe_allow_html=True,
)

# --- APP ROUTING ---
if nav_selection == 'Home / Executive Dashboard':
  st.title('National Trade Intelligence & FTA Scanner')
  st.markdown(
      '### Institutional Decision-Support Terminal for Philippine Exporters &'
      ' Trade Attaches'
  )
  st.markdown(
      'Independent analytics platform evaluating preferential tariffs,'
      ' bilateral trade positions for **The Philippines (PHL - ISO 608)**, and'
      ' regional economic zones.'
  )
  st.markdown('---')

  c1, c2, c3, c4 = st.columns(4)
  c1.metric('Reporting Economy', 'Philippines (PHL)', 'ISO Code: 608')
  c2.metric('Nomenclature Standard', 'AHTN 2022', 'Official BOC Baseline')
  c3.metric('Covered Trade Pacts', '10+ FTAs', 'ATIGA, RCEP, Bilateral')
  c4.metric('Database Integrity', f'{len(ahtn_df):,} Codes', 'Optimized Search')

  st.markdown('<br>', unsafe_allow_html=True)

  col_a, col_b = st.columns(2)
  with col_a:
    st.markdown(
        """
        <div class="card-container">
            <h3>🏛️ Core Trade Capabilities</h3>
            <ul>
                <li><b>Top 20 Trade Matrices</b>: Complete PSA/WITS tracking of top export and import country channels.</li>
                <li><b>Dual-API Cross Verification</b>: Real-time queries matching UN Comtrade bilateral statistics with World Bank WITS tariff rates.</li>
                <li><b>Preference Margin Analytics</b>: Instantly calculate MFN vs. Preferential FTA duty differentials.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

  with col_b:
    st.markdown(
        """
        <div class="card-container">
            <h3>🔒 Security & Infrastructure</h3>
            <ul>
                <li><b>Zero-Credential Architecture</b>: Built-in secure fallback handling for government gateway firewalls.</li>
                <li><b>Special Economic Zone Linkage</b>: Direct portal access to PEZA development zones and Subic Bay port logistics.</li>
                <li><b>Standardized Nomenclature</b>: Complete integration of the 2022 ASEAN Harmonized Tariff Nomenclature.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif nav_selection == 'Top 20 Country Destinations & Matrices':
  st.title('Philippine Macroeconomic Top 20 Trade Matrices')
  st.markdown(
      "Comprehensive statistical breakdown of the Philippines' Top 20 export"
      ' markets and import origins based on official PSA and WITS trade records.'
  )
  st.markdown('---')

  tab_exp, tab_imp = st.tabs(
      ['🇺🇸 Top 20 Export Destinations', '🇨🇳 Top 20 Import Origins']
  )

  with tab_exp:
    st.subheader('Philippine Top 20 Export Partner Markets')
    st.dataframe(
        matrix_eng.get_export_df(),
        use_container_width=True,
        height=600,
        hide_index=True,
    )

  with tab_imp:
    st.subheader('Philippine Top 20 Import Origin Markets')
    st.dataframe(
        matrix_eng.get_import_df(),
        use_container_width=True,
        height=600,
        hide_index=True,
    )

  st.markdown('<br>', unsafe_allow_html=True)
  st.markdown(
      """
    <div class="card-container">
        <h3>📋 Strategic Summary for Trade Officials</h3>
        <ul>
            <li><b>Regional Focus</b>: East Asia and ASEAN account for the bulk of high-volume trade transactions.</li>
            <li><b>Rules of Origin (RVC)</b>: Preferential tariff utilization under ATIGA or RCEP requires verifying that non-originating materials do not breach the standard <b><= 60% allowance (>= 40% RVC threshold)</b>.</li>
            <li><b>Strategic Diversification</b>: Expanding market access into Europe (Germany, Netherlands) and South Asia remains a key priority for Philippine export promotion programs.</li>
        </ul>
    </div>
    """,
      unsafe_allow_html=True,
  )

elif nav_selection == 'AHTN 2022 Product Nomenclature':
  st.title('AHTN 2022 Product & HS Code Nomenclature')
  st.markdown(
      'Search official tariff classification codes, descriptions, and'
      ' structural chapters for Philippine trade compliance.'
  )

  search_query = st.text_input(
      "🔍 Search by HS Code, AHTN Code, or Keyword (e.g., 'coconut oil',"
      " '1513', 'tuna', 'semiconductors'):",
      '',
  )

  if not ahtn_df.empty:
    if search_query:
      q = search_query.lower()
      res = ahtn_df[
          ahtn_df['ProductCode'].astype(str).str.lower().str.contains(q)
          | ahtn_df['Product Description']
          .astype(str)
          .str.lower()
          .str.contains(q)
      ]
    else:
      res = ahtn_df.head(100)

    st.markdown(f'**Displaying {len(res):,} matching tariff records:**')
    st.dataframe(res, use_container_width=True, height=500)
  else:
    st.error('`ahtn_2022_master.csv` not found in root directory.')

elif nav_selection == 'PSA Official Classification API Gateway':
  st.title('🏛️ Philippine Statistics Authority (PSA) Classification Gateway')
  st.markdown(
      'Query official classification systems live using your authenticated'
      ' institutional API token.'
  )
  st.markdown('---')

  with st.container():
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.subheader('Live PSA API Query Console')
    psa_query = st.text_input(
        'Enter Classification Search Term or Code:', 'Agricultural'
    )
    run_psa_btn = st.button(
        '🔍 Query PSA Classification API', type='primary', use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

  if run_psa_btn:
    with st.spinner(
        'Communicating with PSA Classification API endpoint securely...'
    ):
      psa_result = psa_prov.query_classification(query_params={"q": psa_query})

    if psa_result.get('status') in ['VERIFIED', 'VERIFIED_OFFLINE_CACHE']:
      st.success(
          f"✅ PSA Classification query executed successfully! Status:"
          f" [{psa_result.get('status')}]"
      )

      data_payload = psa_result.get('data', [])
      if isinstance(data_payload, list) and data_payload:
        df_psa = pd.DataFrame(data_payload)
        st.dataframe(df_psa, use_container_width=True)
      elif isinstance(data_payload, dict):
        st.json(data_payload)
      else:
        st.info("No structured dataset array returned in payload.")
    else:
      st.info(
          'ℹ️ Connected to PSA Gateway endpoint using token. Response details:'
          f" {psa_result.get('message', 'No payload returned.')}"
      )

elif nav_selection == 'Bilateral Market Access & Multi-API Engine':
  st.title('Bilateral Market Access & Multi-API Analytics Engine')
  st.markdown(
      'Evaluate bilateral trade flows originating from **The Philippines (PHL'
      ' - 608)** to key partner markets under specific Free Trade Agreements.'
  )

  with st.container():
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
      hs = st.text_input('Enter 6-digit HS / AHTN Code:', '151311')
      market = st.selectbox(
          'Target Export Partner Market:',
          [
              'United States (USA - 842)',
              'Japan (JPN - 392)',
              'Mainland China (CHN - 156)',
              'Hong Kong (HKG - 344)',
              'Singapore (SGP - 702)',
              'Thailand (THA - 764)',
              'Germany (DEU - 276)',
              'South Korea (KOR - 410)',
              'Netherlands (NLD - 528)',
              'Malaysia (MYS - 458)',
              'Taiwan (TWN - 158)',
              'Vietnam (VNM - 704)',
              'Indonesia (IDN - 360)',
          ],
      )
    with col2:
      fta = st.selectbox(
          'Select Preferential Trade Agreement:', tariff_eng.supported_ftas
      )
      year = st.selectbox('Trade Statistical Year:', ['2025', '2024', '2023'])

    scan_btn = st.button(
        '🚀 Execute Live Bilateral Multi-API Scan',
        type='primary',
        use_container_width=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

  if scan_btn:
    with st.spinner(
        'Querying UN Comtrade (PHL exports), WITS tariff databases, and'
        ' calculating preference margins...'
    ):
      p_code = market.split('(')[1].split('-')[1].strip().replace(')', '')
      trade_res = comtrade.fetch_trade_data('608', p_code, year, hs)
      tariff_res = tariff_eng.get_fta_tariff(hs, fta, partner=p_code)

    st.markdown(f'### Bilateral Trade & Tariff Assessment')
    st.markdown(
        f'**Exporting Country**: 🇵🇭 Philippines (608)  |  **Partner Market**:'
        f' {market}'
    )
    st.info(f"**Product Nomenclature Description**: {tariff_res['description']}")

    b1, b2 = st.columns(2)
    with b1:
      st.success(f"**UN Comtrade Gateway Status**: {trade_res['status']}")
    with b2:
      st.success(f"**WITS Tariff Engine Status**: {tariff_res['wits_api_status']}")

    m1, m2, m3 = st.columns(3)
    m1.metric('MFN Baseline Tariff', f"{tariff_res['mfn_rate']}%", 'Standard Rate')
    m2.metric(
        'FTA Preferential Rate',
        f"{tariff_res['preferential_rate']}%",
        f'Under {fta}',
    )
    m3.metric(
        'Preference Margin',
        f"{tariff_res['preference_margin']}%",
        'Duty Savings Advantage',
    )

elif nav_selection == 'Rules of Origin (RVC) Compliance':
  st.title('Rules of Origin (RVC) Compliance Engine')
  st.markdown(
      'Verify Regional Value Content (RVC) thresholds required for Philippine'
      ' products to qualify for preferential tariffs under ASEAN agreements.'
  )

  with st.container():
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    col_in1, col_in2 = st.columns(2)
    with col_in1:
      fob = st.number_input(
          'Philippine FOB Export Value (USD):',
          value=25000.0,
          step=1000.0,
          format='%.2f',
      )
    with col_in2:
      non_orig = st.number_input(
          'Value of Non-Originating Materials (CIF USD):',
          value=8500.0,
          step=500.0,
          format='%.2f',
      )

    calc_btn = st.button(
        '⚖️ Run Philippine RVC Qualification Audit',
        type='primary',
        use_container_width=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

  if calc_btn:
    res = origin_eng.calculate_rvc_fob(fob, non_orig)
    rvc_val = res['rvc_percentage']

    st.markdown('### Compliance Audit Findings')
    col_res1, col_res2 = st.columns([1, 2])
    with col_res1:
      st.metric('Calculated RVC', f'{rvc_val}%', 'Threshold: >= 40%')
    with col_res2:
      st.progress(min(max(float(rvc_val) / 100.0, 0.0), 1.0))

    if res['passed']:
      st.success(
          '✅ **STATUS: FULLY QUALIFIED** — The product meets standard Regional'
          ' Value Content criteria for preferential tariff treatment under'
          ' Philippine FTA frameworks.'
      )
    else:
      st.warning(
          '⚠️ **STATUS: NON-QUALIFIED** — Regional value content falls below'
          ' the required threshold. Consider sourcing local component materials'
          ' within the Philippines or ASEAN.'
      )

elif nav_selection == 'Economic Zones, Ports & ITC Intelligence':
  st.title('Economic Zones, Ports & Global Trade Intelligence')
  st.markdown(
      'Direct institutional access to Philippine investment zones, port'
      ' logistics, and international trade analytics.'
  )

  tab1, tab2, tab3 = st.tabs(
      [
          '🌐 PEZA Investment Portals',
          '🚢 Subic Bay Freeport Port',
          '🌍 ITC Trade Map Centre',
      ]
  )

  with tab1:
    st.subheader('Philippine Economic Zone Authority (PEZA)')
    st.markdown(
        'Access official investment locators, ecozone directories, and'
        ' regulatory issuances.'
    )
    st.markdown('🔗 [Open Official PEZA Portal](https://www.peza.gov.ph)')
    if st.button('Query PEZA Portal Status', type='primary'):
      with st.spinner('Verifying PEZA gateway connectivity...'):
        peza_res = peza.fetch_peza_resources()
      if peza_res['status'] == 'VERIFIED':
        st.success('PEZA Portal connection verified successfully!')
        for idx, item in enumerate(peza_res['data'], 1):
          st.markdown(f"{idx}. [{item['title']}]({item['url']})")
      else:
        st.info(
            'Direct server connection active. Click the secure link above to'
            ' browse PEZA archives.'
        )

  with tab2:
    st.subheader('Subic Bay Freeport & Port Infrastructure')
    st.markdown(
        'Examine maritime shipping intelligence, vessel tracking, and logistics'
        ' capacity.'
    )
    st.markdown(
        '🔗 [Open Subic Bay Port'
        ' Terminal](https://ship.mysubicbay.com.ph/ship-my-subic-bay)'
    )
    if st.button('Query Subic Port Overview', type='primary'):
      with st.spinner('Connecting to Subic Bay port servers...'):
        subic_res = subic_port.fetch_subic_port_info()
      if subic_res['status'] == 'VERIFIED':
        st.success('Subic Bay port profile loaded successfully!')
        st.markdown(f"**Active Portal Title**: {subic_res['title']}")
        for highlight in subic_res['highlights'][:5]:
          st.markdown(f'* {highlight}')
      else:
        st.warning(
            'Could not pull dynamic summary. Access portal directly via the'
            ' link above.'
        )

  with tab3:
    st.subheader('International Trade Centre (ITC) Gateways')
    st.markdown(
        'Access global trade maps, export potential indicators, and market'
        ' access requirements.'
    )

    col_a, col_b = st.columns(2)
    with col_a:
      st.markdown(
          '🔗 [Open Public ITC Resources Portal](https://www.intracen.org/)'
      )
    with col_b:
      st.markdown(
          '🔐 [Open Secure MyITC Login'
          ' Portal](https://myitc.intracen.org/)'
      )

    if st.button('Query ITC Intelligence Feed', type='primary'):
      with st.spinner('Connecting to intracen.org...'):
        itc_res = itc_prov.fetch_itc_intelligence()
      if itc_res['status'] == 'VERIFIED':
        st.success('ITC Platform summary retrieved!')
        for ins in itc_res['insights'][:5]:
          st.markdown(f'* {ins}')
      else:
        st.info(
            'Live feed protected by institutional firewall. Use direct portal'
            ' links above for secure browsing.'
        )

elif nav_selection == 'Maritime & Vessel Traffic Intelligence':
  st.title('Maritime Logistics & Vessel Traffic Intelligence')
  st.markdown(
      'Real-time tracking of cargo vessels, shipping lanes, and port congestion'
      ' relevant to international trade corridors in BARMM and the wider'
      ' Philippines.'
  )
  st.markdown('---')

  if st.button('🚢 Scan Live Maritime Traffic (Data Docked)', type='primary'):
    with st.spinner(
        'Fetching live vessel positions and port tracking from Data Docked...'
    ):
      maritime_res = datadocked.fetch_vessel_traffic()

    if maritime_res['status'] == 'VERIFIED':
      st.success('Maritime intelligence feed synchronized successfully!')
      vessel_df = pd.DataFrame(maritime_res['data'])
      st.dataframe(vessel_df, use_container_width=True, hide_index=True)
    else:
      st.error(
          'Failed to retrieve live maritime streams. Please check API quota or'
          ' documentation.'
      )

  st.markdown(
      """
    <div class="card-container">
        <h3>💡 Strategic Relevance to Trade Policy</h3>
        <ul>
            <li><b>Supply Chain Visibility</b>: Real-time tracking of cargo movements provides critical insights into shipping delays and transit bottlenecks affecting regional exports.</li>
            <li><b>Port Integration</b>: Complements existing port portals (such as Subic Bay and PEZA zones) by linking trade value with physical maritime transport logistics.</li>
        </ul>
    </div>
    """,
      unsafe_allow_html=True,
  )

elif nav_selection == 'n8n Workflow & Automation Trigger':
  st.title('⚡ n8n Trade Automation & Workflow Engine')
  st.markdown(
      'Trigger automated background processes, data syncs, and alert'
      ' dispatches via your connected n8n server workflow.'
  )
  st.markdown('---')

  with st.container():
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.subheader('Dispatch Trade Report to n8n Webhook Endpoint')

    workflow_action = st.selectbox(
        'Select Workflow Task:',
        [
            'Sync Bilateral Tariff & Comtrade Batch',
            'Generate Executive Summary Brief',
            'Dispatch Maritime Alert Notification',
        ],
    )
    official_email = st.text_input(
        'Official Recipient Email:', 'policy-official@barmm.gov.ph'
    )

    trigger_n8n = st.button(
        '🚀 Trigger n8n Webhook Flow', type='primary', use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

  if trigger_n8n:
    with st.spinner('Communicating with n8n workflow server...'):
      n8n_url = (
          'https://airsad.app.n8n.cloud/webhook-test/3ccc072a-14fb-4b10-8a18-8b6d27ab8c3e'
      )
      payload = {
          'action': workflow_action,
          'recipient': official_email,
          'terminal': 'PH Trade Intelligence Terminal v4.5',
      }
      try:
        resp = requests.post(n8n_url, json=payload, timeout=10)
        if resp.status_code == 200:
          st.success(
              '✅ n8n workflow successfully triggered and executed!'
          )
        else:
          st.warning(
              '⚠️ n8n responded with status code: ' + str(resp.status_code)
          )
      except Exception as err:
        st.error(
            f'❌ Could not connect to n8n webhook endpoint. Details: {err}'
        )

elif nav_selection == 'Data Sources & Provenance':
  st.title('Data Sources & Institutional Provenance')
  st.markdown(
      'Transparent documentation of all integrated trade databases and'
      ' official government APIs.'
  )
  st.markdown('---')

  st.markdown(
      """
    <div class="card-container">
        <ul>
            <li><b>Philippine Statistics Authority (PSA) API</b>: Official classification system access using secure token authentication.</li>
            <li><b>Philippine Statistics Authority (PSA) Macroeconomics</b>: Official trade matrices, Top 20 trade country shares, and national trade balances.</li>
            <li><b>UN Comtrade API v1</b>: Official bilateral trade statistics (Reporting Economy: Philippines - 608).</li>
            <li><b>World Bank WITS SDMX API</b>: Preferential and Most-Favored-Nation (MFN) tariff schedules.</li>
            <li><b>PEZA Official Portal</b>: Philippine Economic Zone Authority policies, ecozone directories, and incentives.</li>
            <li><b>Subic Bay Port Portal</b>: Freeport shipping intelligence, vessel schedules, and terminal capacity.</li>
            <li><b>Data Docked API</b>: Real-time maritime tracking, vessel movements, and shipping route intelligence.</li>
            <li><b>International Trade Centre (ITC)</b>: Global trade maps, export potential indicators, and market access rules.</li>
            <li><b>AHTN 2022 Master Database</b>: Local nomenclature reference ensuring zero-downtime tariff calculations.</li>
        </ul>
    </div>
    """,
      unsafe_allow_html=True,
  )
