# -*- coding:utf-8 -*-
if __name__ == "__main__":
    directFlag = False
    indirectFlag = False
    a, b, c, d= map(int, input().split())
    if abs(a-c) <= d:
        directFlag = True
    else:
        pass
    if abs(a-b) <= d and abs(b-c) <= d:
        indirectFlag = True
    else:
        pass
    if directFlag or indirectFlag:
        print("Yes")
    else:
        print("No")
