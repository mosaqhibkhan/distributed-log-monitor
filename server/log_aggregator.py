import socket

server = socket.socket()
server.bind(("localhost", 9000))
server.listen(5)

print("Log server running...")

while True:
    client, addr = server.accept()
    log = client.recv(1024).decode()
    print("Received log:", log)
    client.close()