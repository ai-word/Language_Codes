from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7788))#绑定的目的：为了让接收方有一个明确的地址

recvData = udpSocket.recvfrom(1024)

print(recvData)
