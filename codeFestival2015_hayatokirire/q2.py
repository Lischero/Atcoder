# -*- coding:utf-8 -*-
import sys
p = [ list(map(lambda a: True if a == 'o' else False, list(input()))) for _ in range(10) ]
for x in range(10):
    ans = False
    for y in range(10):
        ans = ans or p[y][x]
    if ans:
        pass
    else:
        print("No")
        sys.exit()
print("Yes")
