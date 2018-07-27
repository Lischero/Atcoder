# -*- coding:utf-8 -*-
import sys
if __name__ == "__main__":
    s = list(input())
    t = list(input())
    for tmp in range(0, len(t)):
        factor = []
        factor.append(s.pop())
        factor.extend(s)
        s = factor
        if ''.join(factor) ==''.join(t):
            print("Yes")
            sys.exit(0)
    else:
        print("No")
