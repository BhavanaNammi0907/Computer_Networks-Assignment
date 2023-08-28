from socket import *
myIP = "192.168.0.44"
myPort = 12347
buffer = 1024
FORMAT = "utf-8"
serverMessage = "Message from TCP Client"
sendMessage = str.encode(serverMessage)
# creating a TCP socket on the server side
TCPSocket = socket(AF_INET, SOCK_STREAM)
# binding to server port number
TCPSocket.bind((myIP, myPort))
print("TCP server up and listening")
# allow 10 pending connections
TCPSocket.listen(10)
while True:
    # wait for next client to connect
    connection, address = TCPSocket.accept()
    data = connection.recv(buffer)
    clientMessage = "Message from Client:{}".format(data)
    clientIP = "Client IP Address:{}".format(address)
    print(clientMessage)
    print(clientIP)
    connection.sendto(sendMessage, address)

    filename = connection.recv(buffer).decode(FORMAT)
    print(filename)

    connection.close()
