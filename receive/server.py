import socket
from huffmanDecoding import Decoding 

host = socket.gethostname()
port = 5001
port2 = 5002

s = socket.socket()
s.bind((host, port))

s.listen(5)
print(f"---------- Listening as {host}:{port} ----------")

conn, address = s.accept() 
print("---------- Client connected: ", address)



with open('received.bin', 'wb') as file:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)

    file.close()
conn.close()
s.close()
print("Exit.")

s2 = socket.socket()
s2.bind((host, port2))
s2.listen(5)
conn2, address2 = s2.accept()

with open('keyReceived.txt', 'wb') as file:
    while True:
        data = conn2.recv(1024)
        if not data:
            break
        file.write(data)

    file.close()

d = Decoding('keyReceived.txt','received.bin')
d.decompress()