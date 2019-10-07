#!/usr/bin/env python

import requests

class Test(object):

    def send(self, title, message):
        print(title, message)

def main():
    test = Test()
    test.send('title', 'message')

if __name__ == "__main__":
    main()
