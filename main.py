from src import phone_lookup, photo_recon, username_lookup, email_enum, report_generator
from src.utils import save_json, load_config
import os

def main():
    config = load_config('config/config_sample.json')
    target = input("Enter target (username/email/phone/image path): ").strip()

    results = {}
    if os.path.isfile(target):
        results['photo'] = photo_recon.analyze_photo(target)
    elif '@' in target:
        results['email'] = email_enum.lookup_email(target, config['hibp_api'])
    elif target.isdigit():
        results['phone'] = phone_lookup.lookup_phone(target, config)
    else:
        results['username'] = username_lookup.lookup_username(target)

    save_json(results, f"outputs/results.json")
    report_generator.generate_html_report(results, f"outputs/report.html")
    print("[+] Report generated at outputs/report.html")

if __name__ == '__main__':
    main()
