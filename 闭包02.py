#!/usr/bin/python
# -*- coding: utf-8 -*-  

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此 i 的当前值被传入 f()
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())