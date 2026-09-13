import requests
from bs4 import BeautifulSoup
import urllib3

# Suppress insecure request warnings when verify=False is used
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class PezaProvider:
    def __init__(self):
        self.url = "https://www.peza.gov.ph/downloads?combine=list+of+peza&field_sub_category_downloads_tid=All"
        
    def fetch_peza_resources(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        try:
            # Added verify=False to bypass cloud environment SSL certificate validation errors
            response = requests.get(self.url, headers=headers, timeout=12, verify=False)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                results = []
                for a_tag in soup.find_all('a', href=True):
                    text = a_tag.get_text(strip=True)
                    link = a_tag['href']
                    if text and ('peza' in text.lower() or 'zone' in text.lower() or 'list' in text.lower()):
                        if not link.startswith('http'):
                            link = f"https://www.peza.gov.ph{link}"
                        results.append({"title": text, "url": link})
                
                seen = set()
                unique_results = []
                for r in results:
                    if r['title'] not in seen:
                        seen.add(r['title'])
                        unique_results.append(r)
                        
                return {"status": "VERIFIED", "source": "PEZA Portal", "data": unique_results[:15]}
            else:
                return {"status": "HTTP_ERROR", "message": f"Server status {response.status_code}", "data": []}
        except Exception as e:
            return {"status": "CONNECTION FAILED", "message": str(e), "data": []}
