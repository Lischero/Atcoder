# -*- coding:utf-8 -*-
import sys
N = int(input())
for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n-N*n-N*h != 0:
            w = (N*h*n)//(4*h*n-N*n-N*h)
            if (N*h*n)%(4*h*n-N*n-N*h) == 0 and w > 0:
                print(str(h)+' '+str(n)+' '+str(w))
                sys.exit()
            else:
                pass
        else:
            pass
