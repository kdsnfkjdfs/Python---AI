# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JLzPrn9Cg6ABEGkeLJvDeIZz4-9vOiz9
"""

t1 = ()
t2 = (1,)
print(t2)
print(type(t2))

t4 = (1,2,3)
print(t4)


t5 = 1,2,3
print(t5)

tu = 1,2,3,4,5

print(tu[3])
print(tu[1:4])
print(tu+(6,7))
print(tu*2)

import time
time.localtime()

now =time.localtime()
print(now)

import time

def gettime():
  now = time.lacaltime()
  return now.tm_hour, now.tm_min

hour, min = now.tm_hour, now.tm_min
print(hour, min)

d, m = divmod(7,3)
print(d)
print(m)

score = [ 88,95,70,100,99]

print(score)

tu = tuple(score)
print(tu)