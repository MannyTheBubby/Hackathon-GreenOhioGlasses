import socket 
s = socket.socket()
host = input(str("Please eenter the host address of the sender: "))
port = 8080
s.connect((host,port))
print("Connected!")


filename = input(str("Please enter the filename of the file you with to receive: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close
print("File Transfer Successful!!")


# ---------------------------------------------------------------


import socket
import os
from Crypto.Cipher import AES
import hashlib

s = socket.socket ()
host = socket.gethostname ()
port = 8080
s.bind ((host,port))
s.listen()
print(host)
print("Waiting for incoming traffic. . . ")
conn, addr = s.accept()
print(addr, "Has connected to srvr")

filename = input(str("Please enter a file you wish to transfer: ")) 
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transferred!")