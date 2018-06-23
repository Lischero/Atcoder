# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = input()
    a = list(map(int, list(n)))
    ans = int(n)%sum(a)
    if ans:
        print("No")
    else:
        print("Yes")
