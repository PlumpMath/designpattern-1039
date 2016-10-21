#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def oper(cls):
    def _oper(func):
        def __oper():
            func()
            cls.status()
            print('Done.')
        return __oper
    return _oper
class item:
    def __init__(self):
        print('Init an item.')
    @staticmethod
    def status():
        print('Here is an item.')
@oper(item)
def display():
    print('Start')
if __name__ == '__main__':
    display()

