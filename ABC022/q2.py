# -*- coding:utf-8 -*-
N = int(input())
A = {}
ans = 0
for tmp in range(N):
    tmp2 = int(input())
    if A.get(tmp2,0):
        ans += 1
    else:
        A[tmp2] = 1
print(ans)

'''
for tmp in range(N):
    A.append(int(input()))
for tmp in list(set(A)):
    tmp2 = A.count(tmp)-1
    if tmp2 >= 1:
        ans += tmp2
    else:
        pass
'''
