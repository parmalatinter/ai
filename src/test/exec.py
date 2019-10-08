#!/usr/bin/env python

import requests

class Test(object):

    def send(self, title, message):
        print(title, message)

def AND(x1, x2):
    w1, w2, theta = 1, 1, 0
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
       return 0 
    elif tmp > theta:
       return 1


def main():
    # test = Test()
    # test.send('title', 'message')
    print(AND(0, 0)) # 0 を出力
    print(AND(1, 0)) # 0 を出力
    print(AND(0, 1)) # 0 を出力
    print(AND(1, 1)) # 1 を出力

if __name__ == "__main__":
    main()
