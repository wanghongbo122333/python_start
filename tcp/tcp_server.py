# socket就是一个网络通讯协议
# 服务器端  模拟tcp服务器端发送组包完成后的数据

import socket
import time


ip = '127.0.0.1'
port = 6677
isOK=False

while not isOK:
    server = socket.socket()
    server.bind((ip, port))  # 绑定要监听的端口
    server.listen()  # 监听

    print('组包完成，待发送..')
    # 在这里会形成阻塞,一直等到有客户连接
    # conn就是客户端连过来而在服务器内生成的一个连接实例
    conn, address = server.accept()  # 等电话打进来
    print('准备发送数据：')
    isOK=True
    try:
        while True:
            try:
                # data = conn.recv(65536)  # 官方要求最好不要高于8192 - 8k
                # print(data)
                # conn.send("You have connected to tcp server".encode('utf-8'))
                ''' 
                1、特高频模拟数据[3+101]
                0bc10820f87e(大端) + 0010(2个) + 0(不分片)+ 000（监测） +  0c00-33336340 9701-0c0000-f5280e42 5c8f0342 66660e42 
                
                0bc10820f87e200c003333634097010c0000f5280e425c8f034266660e42
                
                2、高频电流模拟数据[3+102]
                8e00084002cc(大端) + 0010(2个) + 0(不分片) + 000（监测） + 0c00-b81e6540 9b01-080000-00005642 66666642
                
                8e00084002cc200c00b81e65409b010800000000564266666642
                
                3、超声模拟数据[3+103]
                8e00084004d7(大端) + 0010(2个) + 0(不分片) + 000（监测） + 0c00-ae476140 9f01-100000-cccc0c42 99993742 33335d42 33337742
                
                8e00084004d7200c00ae4761409f01100000cccc0c429999374233335d4233337742
        
                4、三合一[3+38+103+104]
                8e00084004da(大端) + 0100(4个) + 0(不分片) + 000（监测） + 0c00-0ad76340/9800-33330f42/9f01-100000-cccc0c42 99993742 33335d42 33337742/a301-030000-99198643 33338f43 cccc4943
                
                8e00084004da400c000ad76340980033330f429f01100000cccc0c429999374233335d4233337742a3010c00009919864333338f43cccc4943
                '''

                # 特高频模拟数据
                str_testhex_low_1 = '0bc10820f87e200c003333634097010c0000f5280e425c8f034266660e42'
                # 高频电流模拟数据
                str_testhex_low_2 = '8e00084002cc200c00b81e65409b010800000000564266666642'
                # 超声模拟数据
                str_testhex_low_3 = '8e00084004d7200c00ae4761409f01100000cccc0c429999374233335d4233337742'
                # 三合一
                str_testhex_low_4 = '8e00084004da400c000ad76340980033330f429f01100000cccc0c429999374233335d4233337742a3010c00009919864333338f43cccc4943'

                conn.send(bytes.fromhex(str_testhex_low_1))
                print('特高频模拟数据已发送')
                time.sleep(5)
                conn.send(bytes.fromhex(str_testhex_low_2))
                print('高频电流模拟数据已发送')
                time.sleep(5)
                conn.send(bytes.fromhex(str_testhex_low_3))
                print('超声模拟数据已发送')
                time.sleep(5)
                conn.send(bytes.fromhex(str_testhex_low_4))
                print('三合一数据已发送')
                time.sleep(6)

            except Exception:
                print("disconnect")
                conn, address = server.accept()  # 等电话打进来
            # print('receive:', data)
            # conn.send(data.upper())
    except Exception as e:
        print(e)
        server.close()
