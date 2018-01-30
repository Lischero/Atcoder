# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    a = [ list(map(int, input().split())) for _ in range(2) ]
    ans = float('-inf')
    for x1 in range(1,n+1):
        factor = sum(a[0][0:x1])
        for x2 in range(x1-1,n):
            ans = max(ans, factor+sum(a[1][x2:n+1]))
    print(ans)
