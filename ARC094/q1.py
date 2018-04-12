# -*- coding:utf-8 -*-
def check(num):
    if num%2:
        return 1
    else:
        return 0

if __name__ == "__main__":
    factors = list(map(int, input().split()))
    maximum = max(factors)
    if check(maximum*3) != check(sum(factors)):
        maximum += 1
    else:
        pass
    print(int(((maximum*3)-sum(factors))/2))
