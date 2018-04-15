# -*- coding:utf-8 -*-
if __name__ == "__main__":
    a,b,x = map(int, input().split())
    if a <= x and a+b >= x:
        print("YES")
    else:
        print("NO")
