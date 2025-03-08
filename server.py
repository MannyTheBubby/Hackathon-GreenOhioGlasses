import socket
from Crypto.Cipher import AES
import hashlib

BUFFER_SIZE = 4096 
KEY = b'secure_key_16_bytes'

def decrypt_file(data, key):
    nonce = data[:16]
    cipher = AES.new(hashlib.sha256(key).digest(), AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(data[16:])  

def receive_file(): 
    s = socket.socket()
    host = input("Please enter the host address of the sender: ")
    port = 8080

    try: 
        s.connect((host, port))
        print("Connected!")

        filename = input("Please enter the filename of the file you wish to receive: ")
        with open(filename, 'wb') as file: 
            while True:
                file_data = s.recv(BUFFER_SIZE)
                if not file_data:
                    break
                decrypted_data = decrypt_file(file_data, KEY)
                file.write(decrypted_data)

        print("File Transfer Successful!!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if s:
            s.close()

if __name__ == "__main__":
    receive_file()
