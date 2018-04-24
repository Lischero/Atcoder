# -*- coding:utf-8 -*-
if __name__ == "__main__":
    a, b, c, x, y = map(int, input().split())
    ans = float('inf')
    for tmp in range((10**5)+1):
        ans = min(ans, a*max(0, x-tmp)+b*max(0,y-tmp)+c*2*tmp)
    else:
        print(ans)
