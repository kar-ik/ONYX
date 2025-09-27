# ONYX - Open-Source OSINT Aggregator (CLI)

A lightweight CLI tool for ethical OSINT, collecting public data from sources like Google and HaveIBeenPwned.

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
