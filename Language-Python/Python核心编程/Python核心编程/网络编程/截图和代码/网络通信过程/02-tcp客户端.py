from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("192.168.119.153", 8989))

#注意：
# 1. tcp客户端已经链接好了服务器，所以在以后的数据发送中，不需要填写对方的iph和port----->打电话
# 2. udp在发送数据的时候，因为没有之前的链接，所依需要　在每次的发送中　都要填写接收方的ip和port－－－－－＞写信　
clientSocket.send("haha".encode("gb2312"))

recvData = clientSocket.recv(1024)

print("recvData:%s"%recvData)

clientSocket.close()
