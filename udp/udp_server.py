#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/9/1
# Comment: udp client  模拟路由
import socket
import time

PORT = 5000
# socket.AF_INET 指明使用INET地址集，进行网间通讯
# socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('', PORT)
server_socket.bind(address)
server_socket.settimeout(10)
while True:
    try:
        now = time.time()
        # 接收客户端传来的数据 recvfrom接收客户端的数据，默认是阻塞的，直到有客户端传来数据
        # recvfrom 参数的意义，表示最大能接收多少数据，单位是字节
        # receive_data表示接受到的传来的数据,是bytes类型
        # client  表示传来数据的客户端的身份信息，客户端的ip和端口，元组
        receive_data, client = server_socket.recvfrom(65535)
        print(time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(now)))  # 指定格式打印
        print('我是路由，我收到了来自客户端%s,发送的%s\n' % (client, "分片数据ack"))
    except socket.timeout:
        print("time out")
