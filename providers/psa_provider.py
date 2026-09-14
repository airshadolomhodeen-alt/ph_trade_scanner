import os
import requests
import streamlit as st


class PSAProvider:

  def __init__(self):
    try:
      self.token = st.secrets["PSA_API_TOKEN"]
    except Exception:
      self.token = os.getenv(
          "PSA_API_TOKEN", "5e05d993-a8b9-4f1c-8e5b-6c02b7ba45d3"
      )

    # Use the specific endpoint path from your documentation if available
    self.base_url = "https://psa.gov.ph/api/classification"

  def query_classification(self, keyword_or_code):
    headers = {
        "Authorization": f"Bearer {self.token}",
        "Accept": "application/json",
        "User-Agent": "PH-Trade-Intelligence-Terminal/4.5",
    }
    params = {"query": keyword_or_code}

    try:
      response = requests.get(
          self.base_url, headers=headers, params=params, timeout=10
      )
      if response.status_code == 200:
        return {"status": "VERIFIED", "data": response.json()}
      elif response.status_code == 403:
        return {
            "status": "FORBIDDEN",
            "message": (
                "Access forbidden (403). Please verify if the API base URL"
                " path requires a specific subdomain or alternative header"
                " format in your documentation."
            ),
        }
      else:
        return {
            "status": "ERROR",
            "message": f"API returned status code {response.status_code}",
        }
    except Exception as e:
      return {"status": "EXCEPTION", "message": str(e)}
