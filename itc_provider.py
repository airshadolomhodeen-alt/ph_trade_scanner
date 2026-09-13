import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ItcProvider:
    def __init__(self):
        self.url = "https://www.intracen.org/resources/data-and-analysis"
        self.login_url = "https://myitc.intracen.org/"
        
    def fetch_itc_intelligence(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        try:
            response = requests.get(self.url, headers=headers, timeout=12, verify=False)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.find('title').get_text(strip=True) if soup.find('title') else "ITC Trade Intelligence"
                
                features = []
                for meta in soup.find_all(['h2', 'h3', 'p']):
                    txt = meta.get_text(strip=True)
                    if len(txt) > 30 and txt not in features:
                        features.append(txt)
                        
                return {
                    "status": "VERIFIED",
                    "source": "International Trade Centre (ITC)",
                    "title": title,
                    "insights": features[:6],
                    "url": "https://www.intracen.org/",
                    "myitc_portal": self.login_url
                }
            else:
                return {
                    "status": "HTTP_ERROR",
                    "message": f"Server status code {response.status_code}",
                    "url": "https://www.intracen.org/"
                }
        except Exception as e:
            return {
                "status": "CONNECTION FAILED",
                "message": str(e),
                "url": "https://www.intracen.org/"
            }
