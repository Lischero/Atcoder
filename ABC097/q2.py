# -*- coding:utf-8 -*-
if __name__ == "__main__":
    x = int(input())
    ans = float('-inf')
    for p in range(1,x+1):
        for b in range(2, x+2):
            if p**b <= x:
                ans = max(ans, p**b)
            else:
                break
    else:
        print(ans)

