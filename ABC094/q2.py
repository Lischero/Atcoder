# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n, m, x = map(int, input().split())
    factors = [ tmp for tmp in range(n+1) ]
    gateFlag = [ False for tmp in range(n+1) ]
    a = list(map(int, input().split()))
    for tmp in range(m):
        gateFlag[a[tmp]] = True
    ansFactor = 0
    ansFactor2 = 0
    pivot = x
    while pivot-1 > 0:
        if gateFlag[pivot-1]:
            ansFactor += 1
        else:
            pass
        pivot -= 1
    else:
        pivot = x
    while pivot+1 < n:
        if gateFlag[pivot+1]:
            ansFactor2 += 1
        else:
            pass
        pivot += 1
    print(min(ansFactor, ansFactor2))
