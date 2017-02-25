# -*- coding:utf-8 -*-
import fractions
import math
a, b, n = (int(input()), int(input()), int(input()))
c = a*b // fractions.gcd(a, b)
print(c*math.ceil(n/c))
