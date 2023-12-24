#echoclient.py
import socket
port = 1235
address = '127.0.0.1'
BUF_SIZE = 2048

# create a socket object name 'con'
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))

message = "1"*2048
con.send(bytes(message,"utf-8"));

data = con.recv(1)

con.close()
print(data.decode("utf-8"))
print(len(data))

