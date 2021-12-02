import socket

sender = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
sender.sendto(str.encode('hello Sender'),('192.168.16.42',7779))