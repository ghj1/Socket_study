import cv2 as cv
import socket

cap = cv.VideoCapture(0)
sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 480 * 640 * 3 / 20 = 46080
perlength = int( (480 * 640 * 3) / 20) # 패킷 사이즈
reallength = perlength + 1 # 


while cap.isOpened():
    ret,frame = cap.read()
    cv.resize(frame,(480,640))
    flat = frame.flatten()
    str = flat.tostring()

    for i in range(3):
        sender.sendto(bytes([i]) + str[i*perlength:(i+1)*perlength], ('192.168.16.42', 7778)) # 앞엔 숫자+내용,ip주소
        pass
    pass