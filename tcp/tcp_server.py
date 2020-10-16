# socket就是一个网络通讯协议
# 服务器端  模拟tcp服务器端发送组包完成后的数据

import socket
import time

ip = '127.0.0.1'
port = 6677
server = socket.socket()
server.bind((ip, port))  # 绑定要监听的端口
server.listen()  # 监听

print('组包完成，待发送..')
# 在这里会形成阻塞,一直等到有客户连接
# conn就是客户端连过来而在服务器内生成的一个连接实例
conn, address = server.accept()  # 等电话打进来
while True:
    print('电话来了')
    time.sleep(3)
    try:
        # data = conn.recv(65536)  # 官方要求最好不要高于8192 - 8k
        # print(data)
        msg2 = b'Z\xfd\xa0\x00\x00\x00\x00\x05\x04i\x08\x04\x945\x04i\x08\x04\x945p\x0c\x002VQ@(\x01\xad1\xa495\x01\x02\x00\x00H\x00\x00e\x0540\x01\x1a\xd3\xe6BL\x00\xcf\xa0\x8c4P\x00\xbfF\xc93\x7f\xa4'

        mm = bytes.fromhex('0bc10820f87e409800e5bb854161ea042220030065ea040b0b363069ea044b48b2401320')  # 1320
        mm_cut = mm[:-2]
        # 切掉2字节msg2的crc校验位
        msg2 = msg2[:-2]
        # conn.send("You have connected to tcp server".encode('utf-8'))

        # 模拟组包完之后的数据
        total_data = b'Z\xfd\xa0\x00\x00\x00\x00\x05\x8e\x00\x08@\x02\xb0\x8e\x00\x08@\x02\xb0\x18\x81\x85\xf3\x03A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A' \
                     b'\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00' \
                     b'\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00' \
                     b'\xa0A\x00\x00\xa0A\x00\x00\xa0A\x00\x00\x1bg '
        # 去掉网络帧头和crc
        for_lss_decode = total_data[8:-2]

        conn.send(for_lss_decode)
        print('sended:', for_lss_decode)
    except ConnectionResetError:
        print("disconnect")
        conn, address = server.accept()  # 等电话打进来
    # print('receive:', data)
    # conn.send(data.upper())

server.close()
