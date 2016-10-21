#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# simple example of closure.


def addx(x):
    def function(y):
        return x+y
    return function

# The same as this:
# def addr(x):
#    return lambda y: x+y

add8 = addx(8)
add9 = addx(9)

add8 = add8(100)

print add8
print add9(100)
