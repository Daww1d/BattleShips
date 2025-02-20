import socket

PORT = 9090 #Choose port number
HOST = socket.gethostbyname(socket.gethostname()) #Gets host IP address dynamically / Can specify local if needed

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST , PORT))

server.listen()

while True:
    communication_socket , address = server.accept() #Gets clients address and socket to talk to client
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
