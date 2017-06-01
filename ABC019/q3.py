# -*- coding:utf-8 -*-
def check(num):
    while num%2 == 0:
        num //= 2
    return num
N = int(input())
a = list(map(int, input().split()))
b = list(set(map(lambda x:check(x), a)))
print(len(b))
