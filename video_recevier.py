import socket

recevier = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
recevier.bind(('192.168.16.23',7778))

# 480 * 640 * 3 / 20 = 46080 
perlength = int( (480 * 640 * 3) / 20) 
reallength = perlength + 1 

array = list()

import numpy as np 
import cv2 as cv

while True:
    message, address = recevier.recvfrom(reallength) # recvfrom(값이 length의 값으로 받으면 된다.)
    
    str = message[1:46081]
    num_array = b''
    if message[0] ==19:
        for i in range(20):
            num_array += array[i]

        frame = np.fromstring(num_array, dtype = np.unit8)
        frame = frame.reshape(480,640,3)
        cv.imshow('video receiver', frame)
        pass 

pass
    # message = bytepair[0] 
    # address = bytepair[1]

    # print(message,',',address)
