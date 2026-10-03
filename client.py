import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to server.")

while True:
    message = input("You: ")
    client_socket.sendall(message.encode())

    if message.lower() == "exit":
        break

    data = client_socket.recv(1024)
    print(f"Server: {data.decode()}")

client_socket.close()
