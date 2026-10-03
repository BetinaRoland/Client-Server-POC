# Client-Server-POC
Python Socket Chat (Client-Server)
A simple two-way chat program built with Python's socket module, using TCP.
One program acts as the server and the other as the client. They take turns sending messages.
How it works
server.py creates a TCP socket, binds to 127.0.0.1:65432, listens, and accepts one client.
client.py connects to the same address and port.
The client sends a message, the server prints it and types a reply, and the client prints the reply.
Typing exit from the client closes the connection.
How to run
Open two terminals in this folder.
Terminal 1: python server.py
Terminal 2: python client.py
Concepts used
TCP sockets, client-server model, bind / listen / accept / connect, encode and decode of messages.
Limitations (ideas to improve)
Handles only one client at a time.
Messages go in turns (not real-time).
Works on one computer (localhost) only.
Built by B Betina Roland.