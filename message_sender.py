import socket

sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sender.sendto(str.encode('Hello sender'), ('192.168.16.23', 7778)) #특정한 곳으로 해당하는 것을 보냄(내가 보내는 글자, 보내는 방법, port 번호)
# 풀 때 해당하는 것을 0과 1로 풀기 때문에 ()로 나눠준다.  ->     message = bytepair[0] , address = bytepair[1]
# str.encode는 아스키 값으로 넘어가기 때문에 넣어준다. 

