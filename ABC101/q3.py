# -*- coding:utf-8 -*-
import math
if __name__ == "__main__":
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    print(int(math.ceil((n-k)/(k-1)))+1)
