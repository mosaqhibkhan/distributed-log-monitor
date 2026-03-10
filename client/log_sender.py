import socket

client = socket.socket()
client.connect(("localhost", 9000))

log = "ERROR: Database connection failed"
client.send(log.encode())

client.close()