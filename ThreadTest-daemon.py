#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:whb
# Date:2020/8/31
# Comment: test main thread and sub thread
import threading
import time


def run():
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        t.setDaemon(True)  # 设置守护进程后，主线程结束则各个线程均结束
        thread_list.append(t)

    for t in thread_list:
        t.start()

    print('主线程结束！', threading.current_thread().name)
    print('一共用时：', time.time() - start_time)
