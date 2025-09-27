import requests
from .base import BaseAdapter, Result
from urllib.robotparser import RobotFileParser
from time import sleep

class GoogleAdapter(BaseAdapter):
    name = "google"

    def __init__(self, api_key: str, cx: str):
        self.api_key = api_key
        self.cx = cx
        if not self.api_key or not self.cx:
            raise ValueError("Google API key and CX are required.")
        self.base_url = "https://www.googleapis.com"
        self.rp = RobotFileParser()
        self.rp.set_url(f"{self.base_url}/robots.txt")
        self.rp.read()

    def search(self, query: str, params: Dict) -> Iterator[Result]:
        if not self.rp.can_fetch("*", self.base_url + "/customsearch/v1"):
            raise Exception("Blocked by robots.txt")
        url = f"{self.base_url}/customsearch/v1?key={self.api_key}&cx={self.cx}&q={query}"
        sleep(1)  
        resp = requests.get(url)
        if resp.status_code == 200:
            items = resp.json().get('items', [])
            for item in items:
                yield Result(
                    url=item['link'],
                    title=item['title'],
                    snippet=item['snippet'],
                    raw=item.get('htmlSnippet', ''),
                    timestamp=item.get('pagemap', {}).get('metatags', [{}])[0].get('og:updated_time', ''),
                    metadata={"source": self.name}
                )
        else:
            raise Exception(f"API error: {resp.status_code} - {resp.text}")
