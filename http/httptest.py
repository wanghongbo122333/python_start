#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/11/3
# Comment: for test http request


# import time
# import requests
#
# url = 'http://www.google.com.hk' # 超时
# can_url = 'http://www.baidu.com' # success
#
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# try:
#     html = requests.get(can_url, timeout=5).text
#     print('success')
# except requests.exceptions.RequestException as e:
#     print(e)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'))


import time
import requests
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3)) # 最大尝试次数
s.mount('https://', HTTPAdapter(max_retries=3))

print(time.strftime('%Y-%m-%d %H:%M:%S'))
try:
    r = s.get('http://www.google.com.hk', timeout=5)
    print(r.text)
except requests.exceptions.RequestException as e:
    print(e)
print(time.strftime('%Y-%m-%d %H:%M:%S'))