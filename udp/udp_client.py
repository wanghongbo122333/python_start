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
#     print('Send start', time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(start)))
#     # msg = raw_input("本地客户端192.168.43.131,please input content you want to send")
#     msg = "0bc10820f87e409800e5bb854161ea042220030065ea040b0b363069ea044b48b2401320"
#     s = '5A FD A0 00 00 00 00 01 8E 00 08 40 02 AE 8E 00 08 40 02 AE 18 81 84 F3 03'
#     msg2 = b'Z\xfd\xa0\x00\x00\x00\x00\x05\x04i\x08\x04\x945\x04i\x08\x04\x945p\x0c\x002VQ@(\x01\xad1\xa495\x01\x02\x00\x00H\x00\x00e\x0540\x01\x1a\xd3\xe6BL\x00\xcf\xa0\x8c4P\x00\xbfF\xc93\x7f\xa4'
#     msg3 = b'Z\xfd\xa0\x00\x00\x00\x00\x05\x8e\x00\x08@\x02\xb0\x8e\x00\x08@\x02\xb0\x18A\x81\xf3\x03\x97\x01P8\x00H' \
#            b'\x00\x00\x002\x00\x00\x00\x00\x00\xa0A\x00\x80\x89D\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#            b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xfa9 '
#     total_data = b'Z\xfd\xa0\x00\x00\x00\x00\x05\x8e\x00\x08@\x02\xb0\x8e\x00\x08@\x02\xb0\x18\x81\x85\xf3\x03A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
#                  b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
#                  b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
#                  b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\x1bg '
#     #带网络帧头的数据 crc通过
#     total=b'Z\xfd\xa0\x00\x00\x00\x00\x11\x04i\x08\x04\x94.\x04i\x08\x04\x94.p\x0c\x00\xbf\xa2M@(\x01\x8a\xe2v95\x01\x02\x00\x00H\x00\xe4\xf8\x0540\x01\xafUT\xc1L\x00\xbd\x82l3P\x00+\xe2\xc43\xa4\x8f'
#
#     # print(msg3)
#     #  bind的IP不能随意写，可以不写，可以写本机IP的地址
#     client_socket.sendto(total, (ip, PORT))
#     now = time.time()
#     run_time = now - start
# =======
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
