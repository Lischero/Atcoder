# -*- coding: utf-8 -*-
N,Q = map(int, input().split())
s = [0 for tmp in range(N)]
for tmp in range(Q):
    l, r = map(int, input().split())
    s[ l - 1 ] += 1
    if r < N:
        s[ r ] -= 1 #差分修正用。

for tmp in range(N - 1):
    s[tmp+1] = s[tmp]+s[tmp+1] #累積和を生成。

#終了段階で偶数だったら黒、奇数なら白？
for i in range(N):
    s[i] %= 2
else:
    ans = list(map(str,s))
    print(''.join(ans)) 
