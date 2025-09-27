from typing import Iterator, Dict
from pydantic import BaseModel

class Result(BaseModel):
    url: str
    title: str
    snippet: str
    raw: str
    timestamp: str
    metadata: Dict

class BaseAdapter:
    name: str

    def search(self, query: str, params: Dict) -> Iterator[Result]:
        raise NotImplementedError

    def healthcheck(self) -> Dict:
        return {"status": "healthy", "name": self.name}
