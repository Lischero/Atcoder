# -*- coding:utf-8 -*-
N = int(input())
c = list(map(int, list(input())))
maximum = float('-inf')
minimum = float('inf')
for tmp in range(1, 5):
    factor = len([ tmp2 for tmp2 in c if tmp == tmp2 ])
    maximum = max(maximum, factor)
    minimum = min(minimum, factor)
print(str(maximum)+' '+str(minimum))
