import requests
from typing import Iterator, Dict
from .base import BaseAdapter, Result
from time import sleep

class HIBPAdapter(BaseAdapter):
    name = "hibp"

    def search(self, query: str, params: Dict) -> Iterator[Result]:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{query}"
        headers = {"User-Agent": "ONYX-OSINT-CLI"}
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
                    timestamp=breach.get('BreachDate', ''),
                    metadata={"source": self.name}
                )
        elif resp.status_code == 404:
            return 
        else:
            raise Exception(f"API error: {resp.status_code}")
