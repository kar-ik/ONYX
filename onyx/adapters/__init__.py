from .google import GoogleAdapter
from .hibp import HIBPAdapter

def get_adapters(sources=None, config=None):
    all_adapters = []

    if config.get("GOOGLE_API_KEY") and config.get("GOOGLE_CX"):
        all_adapters.append(
            GoogleAdapter(config.get("GOOGLE_API_KEY"), config.get("GOOGLE_CX"))
        )

    if config.get("HIBP_API_KEY"):
        all_adapters.append(HIBPAdapter(config.get("HIBP_API_KEY")))

    if sources:
        return [a for a in all_adapters if a.name in sources]

    return all_adapters
