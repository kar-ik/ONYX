from .google import GoogleAdapter
from .hibp import HIBPAdapter

def get_adapters(sources=None, config=None):
    all_adapters = [
        GoogleAdapter(config.get('GOOGLE_API_KEY'), config.get('GOOGLE_CX')),
        HIBPAdapter(),
    ]
    if sources:
        return [a for a in all_adapters if a.name in sources]
    return all_adapters
