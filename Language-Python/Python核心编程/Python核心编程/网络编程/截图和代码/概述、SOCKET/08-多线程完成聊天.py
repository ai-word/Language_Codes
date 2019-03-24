from threading import Thread
from socket import *

#1. 收数据，然后打印
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print(">>%s:%s"%(str(recvInfo[1]), recvInfo[0]))

#2. 检测键盘，发数据
def sendData():
    while True:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode("gb2312"), (destIp, destPort))

udpSocket = None
destIp = ""
destPort = 0

def main():
    
    global udpSocket
    global destIp
    global destPort 

    destIp = input("对方的ip:")
    destPort = int(input("对方的ip:"))

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(("", 4567))

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == "__main__":
    main()
