# -*- coding:utf-8 -*-
import itertools
A, B, C, D, E, F = map(int, input().split())
waterWeights = []
sugarWeights = []
ansFactor = []
for tmp in range(F//(100*A)+1):
    for tmp2 in range(F//(100*B)+1):
        factor = 100*A*tmp+100*B*tmp2
        if factor <= F:
            waterWeights.append(factor)
        else:
            pass

for tmp in range(F//C+1):
    for tmp2 in range(F//D+1):
        factor = C*tmp + D*tmp2
        if factor <= F:
            sugarWeights.append(factor)
        else:
            pass

for combi in itertools.product(waterWeights, sugarWeights):
    if combi[0]+combi[1] <= F and combi[0]+combi[1] != 0:
        if E*combi[0]/100 >= combi[1]:
            ansFactor.append(combi)
        else:
            pass
    else:
        pass
ans = sorted(ansFactor, key = lambda i: i[1]*100/(i[0]+i[1]), reverse=True)
print(str((ans[0])[0]+(ans[0])[1])+' '+str((ans[0])[1]))
