import socket
myIP = "192.168.0.44"
myPort = 20001
buffer = 1024

# Creating a UDP socket at the server
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip
UDPSocket.bind((myIP, myPort))
print("UDP server listening")

# Listen for incoming data
count = 0
while True:
    message, address = UDPSocket.recvfrom(buffer)
    serverMessage = str(count)
    sendMessage = str.encode(serverMessage)
    count = count+1
    clientMessage = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)
    print(clientMessage)
    print(clientIP)
    UDPSocket.sendto(sendMessage, address)
