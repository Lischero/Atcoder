# -*- coding:utf-8 -*-
import math
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    factorA = []
    factorB = []
    for index in range(n):
        if a[index] > b[index]:
            factorB.append(a[index]-b[index])
        elif a[index] < b[index]:
            factorA.append((b[index]-a[index])//2)
        else:
            pass
    else:
        if sum(factorA) >= sum(factorB):
            print("Yes")
        else:
            print("No")
