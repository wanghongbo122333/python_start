#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/10/14
# Comment:  模拟组包task，接收数据之后发送ack
import socket
import time

ip = '127.0.0.1'
PORT = 8899  # 接收数据的port
port = 6699  # 接收ack的port
# socket.AF_INET 指明使用INET地址集，进行网间通讯
# socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((ip, PORT))
server_socket.settimeout(10)
while True:
    try:
        now = time.time()
        receive_data = server_socket.recvfrom(65535)
        print("我是组包task，我收到了分片数据：", receive_data)
        # 收到之后 回ack
        sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sendSocket.sendto("我是组包task，组包数据ACK".encode(), 0, (ip, port))

    except socket.timeout:
        print("time out")

server_socket.sendto(str.encode(msg2), (ip, PORT))
