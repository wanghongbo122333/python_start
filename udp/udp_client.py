#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/9/1
# Comment: udp client 模拟发送传感器分片数据
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.7.2"
IP = '192.168.100.10'
localip = "127.0.0.1"
PORT = 8878

while True:
    start = time.time()
    print('Send 微功耗传感器数据', time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(start)))
    # 低功耗数据
    ussdata='44c000000000010bc10820f87e409800e5bb854161ea042220030065ea040b0b363069ea044b48b2401320'

    #  bind的IP不能随意写，可以不写，可以写本机IP的地址
    client_socket.sendto(bytes.fromhex(ussdata), (localip, PORT))
    # now = time.time()
    # run_time = now - start
    # print('send data:', msg3)
    # print('send end time:', time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(now)))
    # print('cost time:', run_time, 's')
    time.sleep(5)
