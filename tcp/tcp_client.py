
# 客户端
import socket
import time

client = socket.socket()  # 声明socket类型和socket链接
# try:
print("start to connect...")
isConnected = False
while not isConnected:  # 没连上
    try:
        print("尝试连接..")
        s = client.connect(('127.0.0.1', 6677))
        isConnected = True
        print("connected")
        # 连接之后开始数据传输
        while True:  # 在这里写死循环 可以让客户端一直保持连接状态而不断开
            msg2 = b'Z\xfd\xa0\x00\x00\x00\x00\x05\x04i\x08\x04\x945\x04i\x08\x04\x945p\x0c\x002VQ@(\x01\xad1\xa495\x01\x02\x00\x00H\x00\x00e\x0540\x01\x1a\xd3\xe6BL\x00\xcf\xa0\x8c4P\x00\xbfF\xc93\x7f\xa4'

            client.send(msg2)  # python3内只能发送比特类型
            time.sleep(5)
            # msg = input('>>:').strip()
            #
            # client.send(msg.encode('utf-8'))  # python3内只能发送比特类型
            #
            # data = client.recv(1024)  # 收多少东西 单位是字节
            #
            # print('receive:', data)
    except Exception:
        isConnected = False


while True:  # 在这里写死循环 可以让客户端一直保持连接状态而不断开
    client.send("hello".encode())  # python3内只能发送比特类型
    time.sleep(5)
    # msg = input('>>:').strip()
    #
    # client.send(msg.encode('utf-8'))  # python3内只能发送比特类型
    #
    # data = client.recv(1024)  # 收多少东西 单位是字节
    #
    # print('receive:', data)

client.close()
