import subprocess
from datetime import datetime


def get_top_cpu_processes(limit=50):
    command = [
        "ps",
        "-arcwwwxo",
        "pid,user,%cpu,rss,comm",
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()[1:]
    processes = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for line in lines[:limit]:
        parts = line.split(None, 4)

        pid = int(parts[0])
        username = parts[1]
        cpu_percent = float(parts[2])
        memory_mb = round(int(parts[3]) / 1024, 2)
        process_name = parts[4]

        processes.append({
            "timestamp": timestamp,
            "process_name": process_name,
            "pid": pid,
            "cpu_percent": cpu_percent,
            "memory_mb": memory_mb,
            "username": username,
        })

    return processes


if __name__ == "__main__":
    top_processes = get_top_cpu_processes()

    for rank, process in enumerate(top_processes, start=1):
        print(
            rank,
            process["process_name"],
            process["pid"],
            process["cpu_percent"],
            process["memory_mb"],
            process["username"],
        )