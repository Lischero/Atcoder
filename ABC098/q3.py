# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    s = list(input())
    ans = float("inf")
    a = [0]+[ 0 if tmp != 'W' else 1 for tmp in s ]
    b = list(reversed([ 0 if tmp != 'E' else 1 for tmp in s ]+[0]))
    for tmp in range(n-1):
        a[tmp+1] += a[tmp]
        b[tmp+1] += b[tmp]
    else:
        a.pop()
        b.pop()
        b = list(reversed(b))
    for tmp in range(n):
        ans = min(ans, a[tmp]+b[tmp])
    else:
        print(ans)
