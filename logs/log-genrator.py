import time
import random

log_file = "../logs/test.log"

messages = [
    "INFO: Task completed successfully",
    "ERROR: Database connection failed",
    "WARNING: Disk space low",
    "ERROR: Failed to process request"
]

while True:
    msg = random.choice(messages)
    with open(log_file, "a") as f:
        f.write(msg + "\n")
    print(f"Generated log: {msg}")
    time.sleep(2) 