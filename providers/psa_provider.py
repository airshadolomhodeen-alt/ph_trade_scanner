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

    # Official PSA Classification domain base URL from your documentation
    self.base_url = "https://classification.psa.gov.ph"

  def query_classification(
      self, classification_type="psoc", version="v1", endpoint="all"
  ):
    """Queries official PSA classification endpoints (PSGC, PSOC, PCOICOP)."""
    url = f"{self.base_url}/api/{classification_type.lower()}/{version}/{endpoint}"

    # PSA APIs typically accept token via Bearer or custom headers/params
    headers = {
        "Authorization": f"Bearer {self.token}",
        "Accept": "application/json",
        "User-Agent": "PH-Trade-Intelligence-Terminal/4.5",
    }

    try:
      response = requests.get(url, headers=headers, timeout=15)
      if response.status_code == 200:
        return {"status": "VERIFIED", "data": response.json()}
      elif response.status_code == 403:
        # Fallback query attempt using token as a query parameter if header is restricted
        alt_response = requests.get(
            url, params={"token": self.token}, timeout=15
        )
        if alt_response.status_code == 200:
          return {"status": "VERIFIED", "data": alt_response.json()}
        return {
            "status": "FORBIDDEN",
            "message": (
                "Access forbidden (403). Please check if the version string"
                " (e.g., v1) matches your documentation parameter."
            ),
        }
      else:
        return {
            "status": "ERROR",
            "message": f"API returned status code {response.status_code}",
        }
    except Exception as e:
      return {"status": "EXCEPTION", "message": str(e)}
