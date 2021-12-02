import socket

recevier = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
recevier.bind(('192.168.16.23',7778))

while True:
    bytepair = recevier.recvfrom(1024)

    message = bytepair[0]
    address = bytepair[1]

    print(message,address)
