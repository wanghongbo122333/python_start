#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/9/29
# Comment:
print("start call so file")
from ctypes import *
test=cdll.LoadLibrary("./selfexamlib——forwindows.so")

print(test.RTU_CRC("whatisyourname",100))