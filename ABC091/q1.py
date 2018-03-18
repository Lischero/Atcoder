# -*- coding:utf-8 -*-
if __name__ == "__main__":
    a, b, c = map(int, input().split())
    if c <= a+b:
        print("Yes")
    else:
        print("No")
