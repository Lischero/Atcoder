# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    a = [0]+list(map(int, input().split()))
    factor = sum([ abs(a[tmp]-a[tmp+1]) for tmp in range(n) ]) + abs(a[-1]-a[0])
    for position in range(1,n+1):
        if position != n: 
            difference = abs(a[position-1]-a[position])+abs(a[position]-a[position+1])
            ans = factor-difference+abs(a[position-1]-a[position+1])
        else:
            difference = abs(a[position-1]-a[position])+abs(a[position]-a[0])
            ans = factor-difference+abs(a[position-1]-a[0])
        print(ans)
