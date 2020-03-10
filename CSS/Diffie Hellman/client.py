"""
Name:Shubham Bhate
roll no:8318
"""
import socket
import dhkeygen

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

key_gen = dhkeygen.DH(23, 5)
msgFromClient = str(key_gen.ABVal(3))
bytesToSend = str.encode(msgFromClient)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}\nK1 = {}".format(int(msgFromServer[0]), key_gen.KeyGen(int(msgFromServer[0]), 3))

print(msg)