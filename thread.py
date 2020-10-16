#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/8/31
# Comment:

import threading


def run():
    print(threading.current_thread().getName())


if __name__ == '__main__':

    th1 = threading.Thread(target=run, name='th1')
    th2 = threading.Thread(target=run, name='th2')
    th1.start()
    th2.start()
