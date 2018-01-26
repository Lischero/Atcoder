# -*- coding:utf-8 -*-
import math
def f(num):
    return math.floor(((num**2)+4)/8)

if __name__ == "__main__":
    print(f(f(f(20))))
