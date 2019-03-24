#coding=utf-8
from socket import *

connNum = raw_input("请输入要链接服务器的次数:")
for i in range(int(connNum)):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("127.0.0.1", 7788))
    print(i)
