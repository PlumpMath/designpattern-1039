#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def deco(func):
    def _deco():
        print("-------Start-------")
        func()
        print("-------Done-------")
    return _deco
@deco
def process1():
    print("This is processs1.")
@deco
def process2():
    print("This is processs2.")

if __name__ == '__main__':
    process1()
    process2()
