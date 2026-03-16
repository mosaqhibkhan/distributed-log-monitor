# server/server.py (with parsing & alerts)
import socket
import threading
from collections import deque
import time

HOST = "127.0.0.1"
PORT = 5000

# Parameters for anomaly detection
ERROR_THRESHOLD = 5        
TIME_WINDOW = 10            
error_times = deque()       

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    while True:
        try:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            print(f"[LOG from {addr}]: {data.strip()}")
            process_log(data.strip())
        except:
            break
    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()

def process_log(log_line):
    """Parse log and detect anomalies"""
    global error_times
    if log_line.startswith("ERROR"):
        now = time.time()
        error_times.append(now)
        # remove errors older than TIME_WINDOW
        while error_times and now - error_times[0] > TIME_WINDOW:
            error_times.popleft()
        if len(error_times) >= ERROR_THRESHOLD:
            print(f"[ALERT] High error rate! {len(error_times)} errors in last {TIME_WINDOW} sec")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()