import random
from datetime import datetime, timedelta

# Some constants
users = ["127.0.0.1"]
endpoints = [
    "/clients",
    "/gigs",
    "/venues",
    "/docs",
    "/openapi.json",
    "/api/users/1",
    "/api/clients/1",
    "/api/venues/1",
]
status_codes = [200, 401, 403]
methods = ["GET", "POST"]
log_sources = [
    "uvicorn.access",
    "uvicorn.error",
    "gigtracker.logger_settings",
]
info_msgs = [
    "Using path gigtracker/app.py",
    "Resolved absolute path /Users/dwesterveld/...",
    "Importing module gigtracker.app",
    "Found importable FastAPI app",
    "Waiting for application startup.",
    "Application startup complete.",
    "Creating venue: Venue",
    "2 changes detected",
]


# Helper to get a timestamp
def timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]


# Generate startup info block
def startup_block():
    return """INFO     Using path gigtracker/app.py
INFO     Resolved absolute path /Users/dwesterveld/personal/Advanced_Scripting_For_Testers/gig-tracker/gigtracker/app.py
INFO     Searching for package file structure from directories with __init__.py files
INFO     Importing from /Users/dwesterveld/personal/Advanced_Scripting_For_Testers/gig-tracker

 ╭─ Python package file structure ─╮
 │                                 │
 │  📁 gigtracker                  │
 │  ├── 🐍 __init__.py             │
 │  └── 🐍 app.py                  │
 │                                 │
 ╰─────────────────────────────────╯

INFO     Importing module gigtracker.app
INFO     Found importable FastAPI app

 ╭───── Importable FastAPI app ─────╮
 │                                  │
 │  from gigtracker.app import app  │
 │                                  │
 ╰──────────────────────────────────╯

INFO     Using import string gigtracker.app:app

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:4001                  │
 │                                                     │
 │  API docs: http://127.0.0.1:4001/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯
"""


def random_datetime(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


# Generate a single log line
def generate_log_line():
    random_time = random_datetime(datetime(2025, 5, 20), datetime(2025, 5, 26))
    src = random.choice(log_sources)
    if src == "uvicorn.access":
        ip = random.choice(users)
        endpoint = random.choice(endpoints)
        status = random.choice(status_codes)
        method = random.choice(methods)
        return f'{random_time} - {src} - INFO - {ip}:{random.randint(50000, 55000)} - "{method} {endpoint} HTTP/1.1" {status}'
    elif src == "uvicorn.error":
        return f"{random_time} - {src} - INFO - {random.choice(['Started server process [20388]', 'Waiting for application startup.', 'Application startup complete.'])}"
    elif src == "gigtracker.logger_settings":
        return f"{random_time} - {src} - INFO - Creating venue: Venue"
    else:
        return f"{random_time} - unknown.logger - INFO - Some generic log message"


# Write a log file
def generate_log_file(filename="fake_log.log", num_lines=50):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(startup_block() + "\n")
        for _ in range(num_lines):
            line = generate_log_line()
            f.write(line + "\n")


if __name__ == "__main__":
    generate_log_file("gigtracker_fake.log", num_lines=1000)
    print("✅ Log file 'gigtracker_fake.log' generated.")
