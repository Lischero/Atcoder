# -*- coding:utf-8 -*-
import sys
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
a = {}
for tmp in range(len(d)):
    if d[tmp] in a:
        a[d[tmp]] += 1
    else:
        a[d[tmp]] = 1
for tmp in range(len(t)):
    if t[tmp] in a:
        if a[t[tmp]] == 0:
            print("NO")
            sys.exit()
        else:
            a[t[tmp]] -= 1
    else:
        print("NO")
        sys.exit()
print("YES")
