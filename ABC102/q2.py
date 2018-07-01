# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(abs(a[0]-a[n-1]))
