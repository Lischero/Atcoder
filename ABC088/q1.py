# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    a = int(input())
    n -= 500*(n//500)
    if n <= a:
        print("Yes")
    else:
        print("No")

