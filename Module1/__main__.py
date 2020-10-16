#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/8/31
# Comment:
import random

i = 1
l = []
while i < 53:
    s = random.randint(50, 300)
    i += 1
    l.append(s)
l.sort(reverse=False)

for i in l:
    print(i)
