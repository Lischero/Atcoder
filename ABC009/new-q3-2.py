# -*- coding:utf-8 -*-
def search(length):
    num = 0
    for tmp in range(length):
        if S[tmp] != T[tmp]:
            num += 1
        else:
            pass
    return num

N, K = map(int, input().split())
S = list(input())
a = sorted(S)
b = sorted(S)
T = []

for tmp in range(N):
    i = []
    for tmp2 in range(len(a)):
        c = b.pop(tmp2)
        e = 0
        d = list((''.join(S))[tmp+1:N])
        for tmp3 in list(set(b)):
            f = b.count(tmp3)
            g = d.count(tmp3)
            e += min(f,g)
        T.append(a[tmp2])
        if T[len(T)-1] != S[len(T)-1]:
            i.append(len(d)-e+1)
        else:
            i.append(len(d)-e)
        T.pop()
        b.append(c)
        b.sort()
    if search(len(T))+i[0] <= K:
        f = a.pop(0)
        b.pop(0)
        T.append(f)
    else:
        f = i.index(min(i))
        g = a.pop(f)
        b.pop(f)
        T.append(g)
print(''.join(T))
