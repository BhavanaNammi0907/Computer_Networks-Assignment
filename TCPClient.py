from socket import *
serverIP = "192.168.0.44"
serverPort = 12347
buffer = 1024
FORMAT = "utf-8"

# creating a TCP socket at the client
count = 0
while True:
    TCPSocket = socket(AF_INET, SOCK_STREAM)
    TCPSocket.connect((serverIP, serverPort))
    clientMessage = str(count)
    sendMessage = str.encode(clientMessage)
    TCPSocket.send(sendMessage)
    count = count + 1
    data = TCPSocket.recv(buffer)
    print(data)

    file = open(("data/demo.txt", "r"))
    data = file.read()

    TCPSocket.send("demo.txt".encode(FORMAT))

    TCPSocket.close()
