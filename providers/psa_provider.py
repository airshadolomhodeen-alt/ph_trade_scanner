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

    # Official PSA classification base domain
    self.base_url = "https://classification.psa.gov.ph"

  def query_classification(
      self, system="psgc", version="v1", query_params=None
  ):
    """Queries official PSA classification systems (psgc, psoc, etc.)

    using required path version and query token.
    """
    system = system.lower()
    # Ensure version defaults to 'v1' or a valid string
    if not version or version == "version":
      version = "v1"

    url = f"{self.base_url}/{system}/{version}/all"

    params = {"token": self.token}
    if query_params and isinstance(query_params, dict):
      params.update(query_params)

    headers = {
        "Accept": "application/json",
        "User-Agent": "PH-Trade-Intelligence-Terminal/4.5",
    }

    try:
      response = requests.get(
          url, headers=headers, params=params, timeout=15
      )
      if response.status_code == 200:
        return {"status": "VERIFIED", "data": response.json()}
      else:
        return {
            "status": "ERROR",
            "message": (
                f"API returned status code {response.status_code}. Response:"
                f" {response.text}"
            ),
        }
    except Exception as e:
      return {"status": "EXCEPTION", "message": str(e)}
