# distributed-log-monitor
Distributed log monitoring system that aggregates logs from multiple services and detects anomalies.

---

## Features
- Real-time log streaming
- Parses `INFO`, `WARNING`, `ERROR`
- Alerts on high error frequency
- Supports multiple agents
- Works on Windows & Linux

---

## Tech Stack
- Python 3
- TCP Sockets
- Multithreading

---

## Project Structure

distributed-log-monitor/
├── agent/agent.py # Log agent
├── server/server.py # Central server
├── logs/test.log # Example log
├── log_generator.py # Log generator
└── README.md

---

## Author

Mohammed Saqhib Uddin Khan
