# -*- coding:utf-8 -*-
rgb = list(input().split())
if int(''.join(rgb))%4 == 0:
    print("YES")
else:
    print("NO")
