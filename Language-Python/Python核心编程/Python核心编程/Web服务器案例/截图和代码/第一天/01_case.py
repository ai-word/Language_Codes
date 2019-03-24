import socket

from socket import *
from math import *

socket = "abc"

server_socket = socket.socket(AF_INET, SOCK_STREAM)

# tcp socket 服务端
socket = socket()
socket.bind()
socket.listen()
cli_socket = socket.accept()
while True:
    p = Process(target=fun, args=())
    p.start()
    cli_socket.close()

def fun(cli_socket):
    # 接收数据
    # request_data = recv()
    # print(request_data)
    # 解析HTTP报文数据 request_data
    # 提取请求方式
    # 提取请求路径path
        HTML_ROOT_DIR= "./html"
        path = /index.html
    /login.html
        try:
            file = open(HTML_ROOT_DIR + "index.html")
        data = file.read()
        file.close()

        except IOError:
"""
    HTTP1.1 404 Not Found\r\n
    \r\n
    not found 
    """






    # 返回响应数据

    """
    HTTP1.1 200 OK\r\n
    \r\n
    hello itcast
    """
    # send()
    # close()

