# -*- coding:utf-8 -*-
import math, itertools
n = int(input())
a = list(itertools.combinations_with_replacement([ tmp for tmp in range(1, int(math.sqrt(n))+10**((int(math.log10(n)+1))//2)) ],2))
print(min([ abs(tmp-tmp2)+(n-tmp*tmp2) for tmp, tmp2 in a if n >= tmp*tmp2 ]))
