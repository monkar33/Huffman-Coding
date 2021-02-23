import socket
import os
from huffmanCoding import Coding 

host = socket.gethostname()
port = 5001
port2 = 5002



print("----------Input file path:----------")

file_path = input()
c = Coding(file_path)
c.compress_file()
file_to_send = 'toSend.bin'

s = socket.socket()

print(f"---------- Connecting to {host} : {port} ----------")

s.connect((host, port))
print("---------- Connected ----------")


with open(file_to_send, "rb") as f:
    while True:
        b = f.read(1024)
        if not b:
            break
        s.sendall(b)

f.close()

s.close()

s2 = socket.socket()
s2.connect((host, port2))
print(f"---------- Connecting to {host} : {port2} ----------")

with open("key.txt", "rb") as f:
    while True:
        b = f.read(1024)
        if not b:
            break
        s2.sendall(b)

f.close()