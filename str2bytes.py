#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:user
# Date:2020/10/14
# Comment:


if __name__ == '__main__':
    b = bytes.fromhex('0bc10820f87e409800e5bb854161ea042220030065ea040b0b363069ea044b48b2401320')
    print(b[4])
    # b = b'\x0b\xc1\x08 \xf8~@\x98\x00\xe5\xbb\x85Aa\xea\x04" \x03\x00e\xea\x04\x0b\x0b60i\xea\x04KH\xb2@\x13 '
    result = str(b)
    print(result[4])

    # result2 = bytes.decode(b)
    # print(result2)

    # result3 = b.hex()
    # print(result3)