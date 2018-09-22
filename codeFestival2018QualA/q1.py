# -*- coding:utf-8 -*-
import itertools
import sys

if __name__ == "__main__":
    a = []
    b = []
    c = []
    a.append(int(input()))
    a.append(a[0]+1)
    b.append(int(input()))
    b.append(b[0]+1)
    c.append(int(input()))
    c.append(c[0]+1)
    s = int(input())
    l = list(itertools.product(a, b, c))
    for tmp in range(len(l)):
        if (sum(l[tmp]) == s):
            print('Yes')
            sys.exit()
    else:
        print('No')
