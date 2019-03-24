from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
#使用ｕｄｐ发送的数据，在每一次的是都需要写上接收方的ip和port
udpSocket.sendto("haha", ("192.168.119.210", 8080))

udpSocket.sendto("haha1", ("192.168.119.210", 8080))
