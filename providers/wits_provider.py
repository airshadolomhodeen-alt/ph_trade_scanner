import streamlit as st
import requests

class WitsProvider:
    def __init__(self):
        # World Bank WITS SDMX REST API base endpoint
        self.base_url = "https://wits.worldbank.org/API/V1/SDMX/V21/rest"
        
    def fetch_tariff_data(self, reporter: str, partner: str, product_code: str):
        """
        Fetches preferential and MFN tariff rates from World Bank WITS API.
        Reporter: ISO numeric or alpha-3 (e.g., 608 or PHL for Philippines)
        Partner: Partner country code or 'WLD' for world
        Product Code: 6-digit HS code
        """
        dataset_id = "DF_WITS_Tariff_TariffLines"
        url = f"{self.base_url}/data/{dataset_id}/A.{reporter}.{partner}.{product_code}.__T"
        
        headers = {
            'Accept': 'application/json'
        }

        try:
            response = requests.get(url, headers=headers, timeout=12)
            
            if response.status_code == 200:
                return {
                    "status": "VERIFIED",
                    "source": "World Bank WITS API",
                    "data": response.json()
                }
            elif response.status_code == 404:
                return {
                    "status": "NO_DATA",
                    "message": "No tariff line entry found for this parameter combination in WITS.",
                    "data": None
                }
            else:
                return {
                    "status": "API ERROR",
                    "message": f"WITS server responded with status code {response.status_code}",
                    "data": None
                }
        except requests.exceptions.RequestException as e:
            return {
                "status": "CONNECTION FAILED",
                "message": str(e),
                "data": None
            }
