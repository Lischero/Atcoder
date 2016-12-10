# -*- coding:utf-8 -*-
import re
s = input()
slist = list(s)

a = 7*(len(re.findall(r"dreamer",s)) - len(re.findall(r"dream",s)))
b = 5*(len(re.findall(r"dream",s)))
c = 6*(len(re.findall(r"eraser",s)) - len(re.findall(r"erase",s)))
d = 5*(len(re.findall(r"erase",s)))
e = len(slist)

if a == 0 and c == 0:
    e -= 1

if a < 0:
    a = 0

if c < 0:
    c = 0

if e == a+b+c+d:
    print("YES")
else:
    print("NO")


