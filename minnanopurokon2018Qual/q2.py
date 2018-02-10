# -*- coding:utf-8 -*-
if __name__ == "__main__":
    x, k = map(int, input().split())
    a = x%10**k
    b = x//10**k
    if not a:
        print(x+10**k)
    else:
        print((10**k)*(b+1))
