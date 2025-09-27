from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()
    return {
        'GOOGLE_API_KEY': os.getenv('GOOGLE_API_KEY'),
        'GOOGLE_CX': os.getenv('GOOGLE_CX'),
        'HIBP_API_KEY': os.getenv('HIBP_API_KEY'),
    }
