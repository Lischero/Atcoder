# -*- coding:utf-8 -*-
'''
def tribonacci(num):
    global l
    if num <= 3 or len(l) >= num:
        return l[num-1]
    if len(l) < num:
        tmp = tribonacci(num-1) + tribonacci(num-2) + tribonacci(num-3)
        l.append(tmp%((10**4)+7))
        return tmp
'''
l = [0,0,1]
n = int(input())
for tmp in range(3,n):
    l.append(l[tmp-1]+l[tmp-2]+l[tmp-3])
    l[tmp] %= (10**4)+7
print(l[n-1])

#print(tribonacci(n)%((10**4)+7))

