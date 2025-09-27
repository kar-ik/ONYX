import requests
from typing import Iterator, Dict, Optional
from .base import BaseAdapter, Result
from time import sleep

class HIBPAdapter(BaseAdapter):
    name = "hibp"

    def __init__(self, api_key: Optional[str] = None):
        if not api_key:
            raise ValueError("HIBP API key is required.")
        self.api_key = api_key

    def search(self, query: str, params: Dict = None) -> Iterator[Result]:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{query}"
        headers = {
            "User-Agent": "ONYX-OSINT-CLI",
            "hibp-api-key": self.api_key
        }
        sleep(1.5)  

        resp = requests.get(url, headers=headers)

        if resp.status_code == 200:
            breaches = resp.json()
            for breach in breaches:
                yield Result(
                    url=f"https://haveibeenpwned.com/PwnedWebsites#{breach['Name']}",
                    title=breach['Name'],
                    snippet=breach['Description'],
                    raw=str(breach),
                    timestamp=breach.get("BreachDate", ""),
                    metadata={"source": self.name}
                )
        elif resp.status_code == 404:
            return  
        else:
            raise Exception(f"HIBP API error: {resp.status_code} - {resp.text}")
