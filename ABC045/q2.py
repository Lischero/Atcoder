# -*- coding:utf-8 -*-
import sys, re
flag = 'a'
def search(sentence):
    global flag
    flag = sentence[0]
    return sentence.replace(flag, '', 1)

S_a, S_b, S_c = (input(), input(), input())

while True:
    if flag == 'a':
        if len(S_a) == 0:
            print("A")
            sys.exit()
        S_a = search(S_a)
    elif flag == 'b':
        if len(S_b) == 0:
            print("B")
            sys.exit()
        S_b = search(S_b)
    else:
        if len(S_c) == 0:
            print("C")
            sys.exit()
        S_c = search(S_c)
