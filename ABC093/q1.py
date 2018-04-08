# -*- coding:utf-8 -*-
if __name__ == "__main__":
    s = list(input())
    if len(list(set(s))) == 3:
        print("Yes")
    else:
        print("No")
