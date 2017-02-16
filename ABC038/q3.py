# -*- coding:utf-8 -*- 
N = int(input())
a = list(map(int, input().split()))
l, ans = (0, N)
while l < N:
    r = l
    if l < N-1 and a[l] < a[l+1]:
        while r < N-1 and a[r] < a[r+1]:
            r += 1
        for tmp in range(1,r-l+1):
            ans += tmp
    l = r + 1
print(ans)
