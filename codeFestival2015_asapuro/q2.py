# -*- coding:utf-8 -*-
N = int(input())
S = list(input())
ans = 0
if len(S)%2 == 0:
    if ''.join(S[0:len(S)//2]) != ''.join(S[len(S)//2:len(S)]):
        for tmp in range(0,len(S)//2):
            if S[tmp] != S[tmp+len(S)//2]:
                ans += 1
            else:
                pass
        print(ans)
    else:
        print(0)
else:
    print(-1)
