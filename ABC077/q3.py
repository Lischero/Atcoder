# -*- coding:utf-8 -*-
import bisect
'''
def search(num,key):
    global n,a,b,c
    left = 0
    right = n-1
    factor = -1
    if num == 1:
        l = a
    else:
        l = c
    while left <= right:
        mid = (left+right)//2
        if key < l[mid]:
            right = mid-1
        elif l[mid] < key:
            left = mid+1
        else:
            if num == 1:
                factor = mid
            else:
                factor = mid+1
            break
    else:
        if factor == -1:
            factor = left
    return factor
'''
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
a.sort()
b.sort()
c.sort()
for tmp in range(n):
    ans += bisect.bisect_left(a,b[tmp])*(n-bisect.bisect_right(c,b[tmp]))
    '''
    ans += search(1, b[tmp])*(n-search(2, b[tmp]))
    '''
print(ans)
