# -*- coding:utf-8 -*-
import itertools
n = int(input())
a = list(map(int, input().split()))
for tmp in range(1,n+2):
    print(len(list(itertools.combinations(a, tmp))))
