import subprocess

def lookup_username(username):
    print("[+] Searching social media profiles...")
    sherlock = subprocess.run(["sherlock", username], capture_output=True, text=True)
    maigret = subprocess.run(["maigret", username], capture_output=True, text=True)
    return {
        "sherlock_output": sherlock.stdout,
        "maigret_output": maigret.stdout
    }
