import os
import cloudscraper
import streamlit as st


class PSAProvider:

  def __init__(self):
    try:
      self.token = st.secrets["PSA_API_TOKEN"]
    except Exception:
      self.token = os.getenv(
          "PSA_API_TOKEN", "5e05d993-a8b9-4f1c-8e5b-6c02b7ba45d3"
      )

    self.base_url = "https://classification.psa.gov.ph"
    # Initialize cloudscraper to bypass Cloudflare bot challenges
    self.scraper = cloudscraper.create_scraper()

  def query_classification(
      self, system="psgc", version="v1", query_params=None
  ):
    """Queries official PSA classification systems using cloudscraper to bypass

    Cloudflare protection.
    """
    system = system.lower()
    if not version or version == "version":
      version = "v1"

    url = f"{self.base_url}/{system}/{version}/all"

    params = {"token": self.token}
    if query_params and isinstance(query_params, dict):
      params.update(query_params)

    try:
      response = self.scraper.get(url, params=params, timeout=20)
      if response.status_code == 200:
        try:
          return {"status": "VERIFIED", "data": response.json()}
        except Exception:
          return {
              "status": "PARSE_ERROR",
              "message": "Response was not valid JSON.",
              "raw": response.text[:300],
          }
      else:
        return {
            "status": "ERROR",
            "message": (
                f"API returned status code {response.status_code}. Response:"
                f" {response.text[:200]}"
            ),
        }
    except Exception as e:
      return {"status": "EXCEPTION", "message": str(e)}
