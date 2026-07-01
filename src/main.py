import os
import time

from dotenv import load_dotenv

from collector import get_top_cpu_processes
from sheets_client import append_processes

load_dotenv()


def main():
    poll_interval = int(os.getenv("POLL_INTERVAL_SECONDS", "10"))

    while True:
        processes = get_top_cpu_processes()
        append_processes(processes)
        print("Top 50 processes written.")
        time.sleep(poll_interval)


if __name__ == "__main__":
    main()