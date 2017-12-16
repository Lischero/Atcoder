# -*- coding:utf-8 -*-
n, m = map(int, input().split())
first = 100*(n-m)+1900*m
average = first/((1/2)**m)
print(int(average))
