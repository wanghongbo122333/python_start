#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/8/31
# Comment: use subclass to implement multi-thread

import threading
import time

count = 0


class Worker(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        print(threading.currentThread().getName())


class Counter(threading.Thread):
    def __init__(self, lock, name):
        self.lock = lock
        super(Counter, self).__init__(name=name)

    def run(self) -> None:
        global count
        self.lock.acquire()
        for i in range(10):
            count = count + 1
            print(count)
        self.lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    for i in range(5):
        Counter(lock, "threading" + str(i)).start()
    time.sleep(2)
    print(count)
