# -*- coding:utf-8 -*-
'''
def LCS(s1,s2,x,y):
    global l
    if s1[x] == s2[y]:
        tmp = max(LCS(s1,s2,x-1,y-1)+1, LCS(s1,s2,x-1,y))
        l[y+1][x+1] = max(tmp, LCS(s1,s2,x,y-1))
    else:
        tmp = max(LCS(s1,s2,x-1,y-1), LCS(s1,s2,x-1,y))
        l[y+1][x+1] = max(tmp, LCS(s1,s2,x,y-1))
'''
n = int(input())
S = []
ans = []
for factor in range(n):
    S.append(input())
for tmp in "abcdefghijklmnopqrstyvwxyz":
    l = []
    for tmp2 in range(n):
        l.append(S[tmp2].count(tmp))
    factor = min(l)
    for tmp3 in range(factor):
        ans.append(tmp)
s = ''.join(ans)
print(s)
'''
for factor in range(n-1):
    l = [[-1 for x in range(len(S[factor])+1)] for y in range(len(S[factor+1])+1)]
    LCS(S[factor],S[factor+1],len(S[factor])-1,len(S[factor+1])-1)
    ans.append(l[len(S[factor+1])-1][len(S[factor])-1])
print(max(ans))
'''
