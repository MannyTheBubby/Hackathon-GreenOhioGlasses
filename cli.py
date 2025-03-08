import socket
from Crypto.Cipher import AES
import hashlib

BUFFER_SIZE = 4096 
KEY = b'secure_key_16_bytes'

def decrypt_file(data, key):
    nonce = data[:16]
    cipher = AES.new(hashlib.sha256(key).digest(), AES.MODE_EAX, nonce=nonce)
    return cipher.encrypt(data[16:])

s = socket.socket()
host = socket.gethostname()
port = 8080

s.bind((host, port))
s.listen()
print(host)

print("Waiting for incoming traffic... ")
conn, addr = s.accept()
print(addr, "Has connected to server")

filename = input("Please enter a file you wish to transfer: ")

try:
    with open(filename, 'rb') as file:
        while True:
            file_data = file.read(BUFFER_SIZE)
            if not file_data:
                break
            encrypted_data = decrypt_file(file_data, KEY)
            conn.send(encrypted_data)
            print("Sending data...")

    print("File Transfer Successful!!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    s.close()
