# -*- coding:utf-8 -*-
if __name__ == "__main__":
    a, b = map(int, input().split())
    ans = 0
    for num in range(a, b+1):
        if str(num) == str(num)[::-1]:
            ans += 1
        else:
            pass
    print(ans)
