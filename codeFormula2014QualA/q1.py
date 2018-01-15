# -*- coding:utf-8 -*-
import sys
a = int(input())
for tmp in range(1,101):
    if a == tmp**3:
        print("YES")
        sys.exit()
    else:
        pass
else:
    print("NO")
