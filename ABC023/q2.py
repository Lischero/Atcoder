# -*- coding:utf-8 -*-
import sys
N = int(input())
S = input()
process_num = (len(S)-1)//2
if S == 'b':
    print(0)
    sys.exit()
elif N%2 != 1 or len(S) == 1:
    print(-1)
    sys.exit()
else:
    count = process_num
    for tmp in range(process_num):
        if count%3 == 1:
            tmp2, tmp3 = ('a','c')
        elif count%3 == 2:
            tmp2, tmp3 = ('c','a')
        else:
            tmp2 = tmp3 = 'b'
        if S[0] == tmp2 and S[-1] == tmp3:
            S = S.lstrip(S[0])
            S = S.rstrip(S[-1])
        else:
            print(-1)
            sys.exit()
        count -= 1
    print(process_num)
