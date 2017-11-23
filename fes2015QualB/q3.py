# -*- coding:utf-8 -*-
import sys
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
a.reverse()
b.sort()
b.reverse()
if n < m:
    print("NO")
else:
    for tmp in range(m):
        if b[tmp] <= a[tmp]:
            pass
        else:
            print("NO")
            sys.exit()
    print("YES")
