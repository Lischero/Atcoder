# -*- coding:utf-8 -*-
N = int(input())
binary = format(N, 'b')
K = 0
ans = []
for tmp in range(len(binary)):
    if binary[tmp] == '1':
        ans.append(2**( len(binary) - tmp - 1 ))
        K += 1
print(K)
for tmp in range(len(ans)):
    print(ans[tmp])
