# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    alice = 0
    bob = 0
    while len(a) > 0:
        a.sort()
        if count%2:
            bob += a.pop()
        else:
            alice += a.pop()
        count += 1
    else:
        print(alice - bob)

