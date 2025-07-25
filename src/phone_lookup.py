from telethon.sync import TelegramClient
from phoneinfo import PhoneInfo

def lookup_phone(number, config):
    print("[+] Gathering phone number details...")
    info = PhoneInfo(number)
    result = {"carrier": info.carrier, "location": info.region, "country": info.country}

    try:
        client = TelegramClient("anon", config['tg_api_id'], config['tg_api_hash'])
        client.connect()
        user = client.get_entity(number)
        result['telegram'] = {"name": user.first_name, "username": user.username}
    except:
        result['telegram'] = "Not found or private"

    return result
