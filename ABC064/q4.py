# -*- coding:utf-8 -*-
import re
N = int(input())
S = input()
a = re.finditer('\(+\)+',S)
b = re.finditer('\){2,}', S)
c = re.finditer('\({2,}', S)
