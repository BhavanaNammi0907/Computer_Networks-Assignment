import socket
clientMessage = "Message from Client"
sendMessage = str.encode(clientMessage)
serverPort = ("192.168.0.206", 20001)
buffer = 1024

# Creating a UDP socket at the client
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Use the UDP socket to send message to server
while (True):
    UDPSocket.sendto(sendMessage, serverPort)
    serverMessage = UDPSocket.recvfrom(buffer)
    message = "Message from Server {}".format(serverMessage[0])
    print(message)
