from socket import *

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    udpSocket.bind(("", 6789))

    #收，打印
    while True:
        recvInfor = udpSocket.recvfrom(1024)
        print("[%s]:%s"%(str(recvInfor[1]), recvInfor[0].decode("gb2312")))


if __name__ == "__main__":
    main()
