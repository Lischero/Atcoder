# -*- coding:utf-8 -*-
N, M = map(int, input().split())
AB = []
friend = []
for tmp in range(M):
    a,b = map(int, input().split())
    AB.append((a,b))
for tmp in range(1,N+1):
    c = []
    for tmp2 in range(M):
        if AB[tmp2][0] == tmp:
            c.append(AB[tmp2][1])
        elif AB[tmp2][1] == tmp:
            c.append(AB[tmp2][0])
        else:
            pass
    friend.append(tuple(c))
for tmp in range(1,N+1):
    ans = []
    if len(friend[tmp-1]) != 0:
        for tmp2 in friend[tmp-1]:
            if len(friend[tmp2-1]) != 0:
                for tmp3 in friend[tmp2-1]:
                    if tmp3 != tmp and tmp not in friend[tmp3-1]:
                        ans.append(tmp3)
    print(len(list(set(ans))))
