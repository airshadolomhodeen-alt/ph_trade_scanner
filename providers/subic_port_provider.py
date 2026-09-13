import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SubicPortProvider:
    def __init__(self):
        self.url = "https://ship.mysubicbay.com.ph/ship-my-subic-bay"
        
    def fetch_subic_port_info(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        try:
            response = requests.get(self.url, headers=headers, timeout=12, verify=False)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract headline title and relevant port highlights/paragraphs
                title = soup.find('title').get_text(strip=True) if soup.find('title') else "Subic Bay Port Intelligence"
                
                content_paragraphs = []
                for p in soup.find_all(['p', 'li']):
                    txt = p.get_text(strip=True)
                    if len(txt) > 40: # Filter meaningful sentences
                        content_paragraphs.append(txt)
                        
                return {
                    "status": "VERIFIED",
                    "source": "Subic Bay Port Portal",
                    "title": title,
                    "highlights": content_paragraphs[:8], # Top relevant highlights
                    "url": self.url
                }
            else:
                return {
                    "status": "HTTP_ERROR",
                    "message": f"Server status code {response.status_code}",
                    "url": self.url
                }
        except Exception as e:
            return {
                "status": "CONNECTION FAILED",
                "message": str(e),
                "url": self.url
            }
