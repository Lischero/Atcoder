# -*- coding:utf-8 -*-
if __name__ == "__main__":
    a, b = map(int, input().split())
    ans = max(a+b, max(a-b, a*b))
    print(ans)
