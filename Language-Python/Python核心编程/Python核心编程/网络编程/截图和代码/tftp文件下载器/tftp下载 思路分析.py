1. 什么叫下载？
2. 怎样完成下载？
	1. 创建一个空文件
	2. 向里面写数据
	3. 关闭
3. 什么叫上传？

udpSocket = socket(...)
udpSocket.bind(...)


f = open("test.jpg","bw")

while True:

	recvData = udpSocket.recvfrom(1024)
	if xxx:
		#没有数据了
		break
	else:
		#收到了数据
		f.write(recvData)



f.close()

4. 怎么发送，怎么接收？
	使用tftp协议

5. 什么样情况下知道了服务器发送完毕呢？
	如果接收到的数据总长度小于516那么意味着 发送完毕

6. 怎样保证一个数字占用2个字节呢？


#不能直接发送字符串
#xxx.sendto("1test.jgp0octet0")



#发送的格式如下：
from socket import *
import struct

#只要是向网络上发送 多个字节表示1个数值的这样的数据，那么就需要pack
#python2
sendData = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)

#python3
sendData = struct.pack("!H8sb5sb",1,"test.jpg".encode("utf-8"),0,"octet".encode("utf-8"),0)

#!表示 组织的数据是用来传递到网络上的，即大端格式
#H表示 占用2个字节
#s表示 一个字符，8s----等价于ssssssss
#b表示 占用1个字节

# udpSocket = socket(AF_INET, SOCK_DGRAM)
# udpSocket.sendto(sendData, ("192.168.119.210", 69))

# udpSocket.close()

#只要是从网络收到了一个 多个字节表示一个值的这样的数据，那么就需要对这个数据进行unpack解析
result = struct.unpack("!HH", recvData[:4])
print(result)




