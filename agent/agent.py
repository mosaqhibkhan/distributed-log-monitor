# agent/agent.py (Windows-friendly)
import time
import os
import socket

# Log file path (relative)
log_file_path = "../logs/test.log"
log_file_path = os.path.abspath(log_file_path)

# Server configuration
SERVER_HOST = "127.0.0.1"  # localhost for testing
SERVER_PORT = 5000

# Connect to server
def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))
    return client

# Tail log file and send to server
def tail_log(file_path, client):
    if not os.path.exists(file_path):
        print(f"Log file does not exist: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        file.seek(0, 2)  # go to end of file
        print(f"Watching log file: {file_path}")
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            line = line.strip()
            print(f"New log: {line}")
            client.sendall(line.encode("utf-8"))

if __name__ == "__main__":
    print("Starting Windows Log Agent...")
    client_socket = connect_to_server()
    tail_log(log_file_path, client_socket)