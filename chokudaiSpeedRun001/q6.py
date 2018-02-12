# -*- coding:utf-8 -*-
if __name__ == "__main__":
    maxNum = 0
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    for tmp in a:
        if maxNum < tmp:
            ans += 1
            maxNum = max(maxNum, tmp)
        else:
            pass
    else:
        print(ans)
