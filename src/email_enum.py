import requests

def lookup_email(email, hibp_key):
    print("[+] Checking email leaks and profile info...")
    hibp_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": hibp_key, "User-Agent": "osint-cli"}
    hibp_res = requests.get(hibp_url, headers=headers)

    gravatar_url = f"https://www.gravatar.com/{email.lower().strip().encode('utf-8').hex()}"
    return {"hibp": hibp_res.json() if hibp_res.status_code == 200 else "No breaches", "gravatar": gravatar_url}
