# -*- coding:utf-8 -*-
import math
N = int(input())
a = list(map(int,input().split()))
alpha, beta = (sum(a), sum(list(map(lambda n:n**2, a))))
beta -= int(alpha**2/N)
print(beta)
