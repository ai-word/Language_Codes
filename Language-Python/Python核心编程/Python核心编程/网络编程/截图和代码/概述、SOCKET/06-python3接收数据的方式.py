from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7789))

recvData = udpSocket.recvfrom(1024)

content, destInfo = recvData

print("content is %s"%content)
print("content is %s"%content.decode("gb2312"))
