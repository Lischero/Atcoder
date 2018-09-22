# -*- coding:utf-8 -*-
import sys
import itertools

if __name__ == "__main__":
    n, m, a, b = map(int, input().split())
    ans = [ 0 for tmp in range(n+1) ]
    out = 0
    for tmp in range(m):
        l, r = map(int, input().split());
        ans[l-1] += 1
        ans[r] -= 1
    for tmp in range(1, n+1):
        ans[tmp] += ans[tmp-1]
    else:
        ans.pop()

    for tmp in range(n):
        if ans[tmp]:
            out += a
        else:
            out += b

    print(out)
