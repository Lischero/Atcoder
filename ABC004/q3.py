# -*- coding:utf-8 -*-
N = int(input())
#to_last = N//5
remaining_task = N%5
l = []
if (N//5)%6 == 0:
    last_num = 6
    l = [ tmp for tmp in range(1,7) ]
else:
    last_num = (N//5)%6
    l = [ tmp for tmp in range(last_num+1, 7) ]
    for tmp in range(1,last_num+1):
        l.append(tmp)

if remaining_task != 0:
    for tmp in range(remaining_task):
        sav = l[tmp]
        l[tmp] = l[tmp+1]
        l[tmp+1] = sav
else:
    pass

l = list(map(str, l))
print(''.join(l))
