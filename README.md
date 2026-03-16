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
├── agent/
│   └── agent.py          # Log agent script
├── server/
│   └── server.py         # Central monitoring server
├── logs/
│   └── test.log          # Example log file
├── log_generator.py      # Optional script to simulate log generation
└── README.md             # Project documentation

---

## Author

Mohammed Saqhib Uddin Khan
