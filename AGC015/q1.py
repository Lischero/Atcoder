# -*- coding:utf-8 -*-
import math
N, A, B = map(int, input().split())
if N != 1 and A <= B:
    '''
    n = math.factorial(B-A+N-2)
    a = math.factorial(N-2)
    b = math.factorial(B-A)
    print(n//(a*b))
    '''
    print((B-A)*(N-2)+1)
else:
    if A != B:
        print(0)
    else:
        print(1)
