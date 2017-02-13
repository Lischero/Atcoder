# -*- coding:utf-8 -*-
import math
n = int(input())
square = math.floor(math.sqrt(n))
ans = min(n - square**2)
