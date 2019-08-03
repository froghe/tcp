# tcp_client.py

import socket

sockfd = socket.socket()

server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

while True:   
    data = input(">>")
    sockfd.send(data.encode())
    if data == '##' or data == '!!':
        break
    data = sockfd.recv(1024)
    print("From server:",data.decode())

sockfd.close()