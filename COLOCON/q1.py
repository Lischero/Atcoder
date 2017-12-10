# -*- coding:utf-8 -*-
a, b = map(int ,input().split())
s = list(input())
if a <= len(s) and len(s) <= b:
    print("YES")
else:
    print("NO")
