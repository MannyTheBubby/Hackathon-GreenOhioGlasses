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
