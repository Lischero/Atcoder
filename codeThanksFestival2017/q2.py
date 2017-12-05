# -*- coding:utf-8 -*-
import sys
s = input()
for t_length in range(len(s)):

    flag = True

    if t_length == 0:
        word = s
    else:
        t = "*"*t_length
        word = s+t

    for tmp in range(len(word)//2):
        if word[tmp] == "*" or word[-1-tmp] == "*":
            continue
        if word[tmp] != word[-1-tmp]:
            flag = False 
            break
    else:
        if flag:
            print(t_length)
            sys.exit()
        else:
            pass
