#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/8/31
# Comment:


def divide(x,y):
    try:
        result = x/y
    except Exception:
        print("Exception occurs")
    finally:
        print("finally executes")


divide(2,1)
divide(2,0)
