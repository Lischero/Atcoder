# -*- coding:utf-8 -*-
import math
N = int(input())
print(min(sorted(list(set([max(int(math.log10(N//B))+1,int(math.log10(B))+1) for B in range(1,int(math.sqrt(N+1))+1) if N%B == 0])))))
