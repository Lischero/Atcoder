# -*- coding:utf-8 -*-
if __name__ == "__main__":
    d, n = map(int, input().split())
    core = 100**d
    factors = [ core*tmp for tmp in range(1,102) if tmp != 100 ]
    print(factors[n-1])
