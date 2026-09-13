import streamlit as st
import requests
import pandas as pd
import io

@st.cache_data
def fetch_psa_openstat_data():
    """Fetches merchandise trade data directly from PSA OpenSTAT API."""
    url = "https://openstat.psa.gov.ph:443/PXWeb/api/v1/en/DB/2E/CS/0012E4EVCP0.px"
    headers = {"Content-Type": "application/json"}
    
    # The JSON query payload matching your Power Query request
    payload = {
        "query": [
            {
                "code": "Year",
                "selection": {
                    "filter": "item",
                    "values": ["37", "38"]
                }
            }
        ],
        "response": {
            "format": "csv"
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            # Read the CSV response text into a Pandas DataFrame
            df = pd.read_csv(io.StringIO(response.text))
            
            # Rename columns to match your desired structure
            if len(df.columns) >= 2:
                df = df.rename(columns={df.columns[0]: "Items", df.columns[1]: "Geolocation"})
            return df
        else:
            st.warning(f"API returned status code: {response.status_code}")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Connection error to PSA OpenSTAT: {e}")
        return pd.DataFrame()

# Example of how to display it inside your Streamlit app page:
def show_psa_data_page():
    st.subheader("📊 Live PSA OpenSTAT Trade Data")
    if st.button("Fetch Live Data from PSA"):
        with st.spinner("Connecting to PSA OpenSTAT API..."):
            df_psa = fetch_psa_openstat_data()
            if not df_psa.empty:
                st.success("Data successfully retrieved from PSA!")
                st.dataframe(df_psa, use_container_width=True)
            else:
                st.info("No data returned or API request failed.")
