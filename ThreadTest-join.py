#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/8/31
# Comment: test join
import threading, time


def run():
    time.sleep(2)
    print('current thread :', threading.current_thread().getName())
    time.sleep(2)


if __name__ == '__main__':
    s_time = time.time()
    print('this is mainThread', threading.current_thread().name)
    threadList = []
    for i in range(10):
        t = threading.Thread(target=run)
        threadList.append(t)
    for t in threadList:
        # t.setDaemon(True)
        t.start()
    # join后，所有线程结束才会结束主线程
    for t in threadList:
        t.join()
    print('main thread over',threading.current_thread().getName())
    print('total time ',time.time()-s_time,'s')