# -*- coding:utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
ans = 0
for num in range(len(a)):
    while True:
        if a[num]%2 == 0 or a[num] == 5:
            a[num] -= 1
            ans += 1
        else:
            break
print(ans)
