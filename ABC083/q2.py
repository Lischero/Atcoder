# -*- coding:utf-8 -*-
n, a, b = map(int, input().split())
ans = 0
for tmp in range(1, n+1):
    c = sum(list(map(int, list(str(tmp)))))
    if c >= a and c <= b:
        ans += tmp
    else:
        pass
else:
    print(ans)
