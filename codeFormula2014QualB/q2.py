# -*- coding:utf-8 -*-
N = list(map(int, list(input())))
N.reverse()
oddSum = 0
evenSum = 0
for tmp in range(len(N)):
    if (tmp+1)%2 == 1:
        oddSum += N[tmp]
    else:
        evenSum += N[tmp]
print(str(evenSum)+' '+str(oddSum))
