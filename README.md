# Google Sheets Automation - Direct Sync  

Automated Python pipeline that collects live CPU and memory telemetry from macOS, synchronizes data with Google Sheets, and visualizes it in Looker Studio dashboards.


## Architecture

macOS → Python → Google Sheets → Looker Studio


## Google Sheets

<img width="620" height="988" alt="image" src="https://github.com/user-attachments/assets/c52a6bbf-7c93-40fe-bfd5-d86d48c2b7e4" />


## Dashboard

<img width="1573" height="948" alt="image" src="https://github.com/user-attachments/assets/fe1b2196-a673-47b6-8183-c05ee2d9f0a8" />


## Features

- Collects live CPU and memory telemetry
- Automatically synchronizes data with Google Sheets
- Supports configurable polling intervals
- Builds real-time dashboards with Looker Studio
- Uses environment variables for secure configuration


## Tech Stack

- Python
- Google Sheets API
- Looker Studio
- gspread
- python-dotenv

## Getting Started

```bash
git clone https://github.com/dcanguven/google-sheets-automation-direct-sync.git
cd google-sheets-automation-direct-sync
pip install -r requirements.txt
```

Create a `.env` file using `.env.example` and place your `service_account.json` file in the `credentials/` directory.

Run:

```bash
python src/main.py
```
