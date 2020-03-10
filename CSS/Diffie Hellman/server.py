"""
Name:Shubham Bhate
roll no:8318
"""
import socket
import dhkeygen

localIP = "127.0.0.1"
localPort = 20001

bufferSize = 1024

key_gen = dhkeygen.DH(23, 5)
msgFromServer = str(key_gen.ABVal(4))
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

#while (True):
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

message = int(bytesAddressPair[0])

address = bytesAddressPair[1]

clientMsg = "Message from Client {}\nK2 :{} ".format(message, key_gen.KeyGen(message, 4))
clientIP = "Client IP Address:{}".format(address)

print(clientMsg)
print(clientIP)

# Sending a reply to client

UDPServerSocket.sendto(bytesToSend, address)