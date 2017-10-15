# -*- coding:utf-8 -*-
a = list(map(int, input().split()))
d = set()
e = [ tmp for tmp in a if tmp in d or d.add(tmp) ]
for tmp in a:
    if tmp not in e:
        print(tmp)
        break
