# -*- coding:utf-8 -*-
import sys
w = input()
for tmp in range (len(w)):
    if w.count(w[tmp])%2 != 0:
        print("No")
        sys.exit()
print("Yes")
