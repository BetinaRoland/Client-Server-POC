import socket

HOST = '127.0.0.1'   # localhost
PORT = 65432          # any free port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode()
    print(f"Client: {message}")

    if message.lower() == "exit":
        break

    reply = input("Server reply: ")
    conn.sendall(reply.encode())

conn.close()
server_socket.close()
print("Server closed.")