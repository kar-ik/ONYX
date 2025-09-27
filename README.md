# ONYX - Open-Source OSINT Aggregator (CLI)

A lightweight CLI tool for ethical OSINT, collecting public data from sources like Google and HaveIBeenPwned.

## Ethical Use

For educational purposes only.
Only use with public data; comply with laws (GDPR, CCPA).
Respects robots.txt and API terms.
Logs saved to onyx.log.
For takedown requests, contact: [tmd772t7y@mozmail.com].

## Features
- Search by email, username, etc.
- Modular adapters (Google, HIBP)
- Text-based timeline
- Export to CSV
- Ethical safeguards (disclaimer, rate-limiting, robots.txt)

## Setup
1. Clone repo: `git clone https://github.com/kar-ik/ONYX.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Get Google API key and CX: [Google Custom Search](https://console.developers.google.com)
4. Copy `.env.example` to `.env` and fill in keys.
5. Initialize DB: Run the following in code_execution tool or manually:
   ```python
   from onyx.storage import init_db
   init_db()

## Usage 
`python -m onyx search "test@example.com" --sources google,hibp --export results.csv`

--sources: Comma-separated (google,hibp). Default: all
--export: Save to CSV file
