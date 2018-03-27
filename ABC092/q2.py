# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    d, x = map(int, input().split())
    ans = 0
    factors = { dayNum:0 for dayNum in range(1, d+1) }
    for tmp in range(n):
        a = int(input())
        factors[1] += 1
        num = 1
        while num*a+1 <= d:
            factors[num*a+1] += 1
            num += 1
    for tmp in range(1, d+1):
        ans += factors[tmp]
    else:
        ans += x
        print(ans)
