# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    s = list(input().split())
    if len(list(set(s))) == 4:
        print("Four")
    else:
        print("Three")

