import streamlit as st
import requests

class ComtradeProvider:
    def __init__(self):
        try:
            self.api_key = st.secrets.get("UN_COMTRADE_KEY", "7cc29a025efc455ca19293fac80e8a52")
        except Exception:
            self.api_key = "7cc29a025efc455ca19293fac80e8a52"
            
        self.base_url = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

    def fetch_trade_data(self, reporter_code: str, partner_code: str, period: str, hs_code: str):
        if not self.api_key:
            return {
                "status": "UNAVAILABLE",
                "message": "UN Comtrade API key not found in configuration.",
                "data": None
            }

        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key
        }
        
        params = {
            'reporterCode': reporter_code,
            'period': period,
            'partnerCode': partner_code,
            'cmdCode': hs_code
        }

        try:
            response = requests.get(self.base_url, headers=headers, params=params, timeout=12)
            
            if response.status_code == 200:
                json_data = response.json()
                return {
                    "status": "VERIFIED",
                    "source": "UN Comtrade API",
                    "data": json_data.get("data", [])
                }
            elif response.status_code == 401:
                return {
                    "status": "UNAUTHORIZED",
                    "message": "Invalid or expired UN Comtrade subscription key.",
                    "data": None
                }
            elif response.status_code == 429:
                return {
                    "status": "RATE_LIMIT_EXCEEDED",
                    "message": "API rate limit reached. Please try again later.",
                    "data": None
                }
            else:
                return {
                    "status": "API ERROR",
                    "message": f"Server responded with status code {response.status_code}",
                    "data": None
                }
        except requests.exceptions.RequestException as e:
            return {
                "status": "CONNECTION FAILED",
                "message": str(e),
                "data": None
            }
