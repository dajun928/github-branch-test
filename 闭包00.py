#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : testttt.py
@time : 2019/09/19 21:29:50
@func : 
"""
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)

print(f())