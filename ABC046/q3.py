# -*- coding:utf-8 -*-
N = int(input())
TA = []
counter = 0
for tmp in range (N):
    TA.append(list(map(int,input().split())))

whole = TA[0][0] + TA[0][1] #総和
for tmp in range (1,N):
    counter = 0
    tmp2 = TA[tmp][0]+TA[tmp][1]
    before = whole/(TA[tmp-1][0]+TA[tmp-1][1]) #比の数値1が何票か。
    while True:
        if (whole+counter)%tmp2 != 0:
            counter += tmp2 - (whole+counter)%tmp2
        whole += counter
        if (before*TA[tmp-1][0] > ((whole/tmp2)*TA[tmp][0]) or (before*TA[tmp-1][1] > ((whole/tmp2)*TA[tmp][1]))):
            counter = 1
            continue
        else:
            break
print(whole)
