# -*- coding:utf-8 -*-
N = int(input())
a = [ int(input()) for tmp in range(N)]
l = sorted(list(set(a)))
dic = { l[index]:index for index in range(len(l)) }
for tmp in range(N):
    a[tmp] = dic[a[tmp]]
    print(a[tmp])
