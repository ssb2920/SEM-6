import socket
import rsa
s=socket.socket()
print('Socket created successfully')
host= socket.gethostname()
port= 12345

s.connect((host, port))
print('Connected successfully')

print(s.recv(1024))
s.close()

