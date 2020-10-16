# __author__ = 'ZSnail'
# 客户端
import socket

client = socket.socket()  # 声明socket类型和socket链接
# try:
print("start to connect...")
s = client.connect(('127.0.0.1', 6677))  # 连接端口
client.getsockopt()
print(s)
while s is not None:
    s = client.connect(('127.0.0.1', 6677))  # 连接端口
# except TimeoutError as e:
#     print(e)
#     client.connect(('127.0.0.1', 6677))
# except ConnectionRefusedError as e:
#     print(e)
#     client.connect(('127.0.0.1', 6677))

while True:  # 在这里写死循环 可以让客户端一直保持连接状态而不断开
    msg = input('>>:').strip()

    client.send(msg.encode('utf-8'))  # python3内只能发送比特类型

    data = client.recv(1024)  # 收多少东西 单位是字节

    print('receive:', data)

client.close()
