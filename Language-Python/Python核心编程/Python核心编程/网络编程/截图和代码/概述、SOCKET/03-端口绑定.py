from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7788))

udpSocket.sendto("haha", ("192.168.119.210", 2426))

