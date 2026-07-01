import os

import gspread
from dotenv import load_dotenv

load_dotenv()


def append_processes(processes):
    spreadsheet_id = os.getenv("GOOGLE_SPREADSHEET_ID")
    worksheet_name = os.getenv("GOOGLE_WORKSHEET_NAME")
    credentials_path = os.getenv("GOOGLE_CREDENTIALS_PATH")

    if not spreadsheet_id:
        raise ValueError("GOOGLE_SPREADSHEET_ID is not set.")

    if not worksheet_name:
        raise ValueError("GOOGLE_WORKSHEET_NAME is not set.")

    if not credentials_path:
        raise ValueError("GOOGLE_CREDENTIALS_PATH is not set.")

    client = gspread.service_account(filename=credentials_path)
    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.worksheet(worksheet_name)

    rows = []

    for rank, process in enumerate(processes, start=1):
        rows.append([
            process["timestamp"],
            rank,
            process["process_name"],
            process["pid"],
            process["cpu_percent"],
            process["memory_mb"],
            process["username"],
        ])

    worksheet.append_rows(rows)