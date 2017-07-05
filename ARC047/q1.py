# -*- coding:utf-8 -*-
N, L = map(int, input().split())
S = list(input())
factor, ans = (1, 0)
for tmp in range(N):
    factor = factor+1 if S[tmp] == '+' else factor-1
    if factor > L:
        factor = 1
        ans += 1
print(ans)
