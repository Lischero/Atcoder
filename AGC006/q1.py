# -*- coding:utf-8 -*-
N = int(input())
s = input()
t = input()
index = N
a = -1
for tmp in range(1,len(t)+1):
    if s[index-1:len(s)] == t[0:tmp]:
        a = index-1
    index -= 1
if a == -1:
    print(len(s+t))
else:
    for tmp in range(len(s)-a, len(t)):
        s = s+t[tmp]
    print(len(s))
