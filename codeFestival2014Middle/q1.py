# -*- coding:utf-8 -*-
import decimal
p, n = map(decimal.Decimal, input().split())
print((1-(1-2*p)**n)/2)
