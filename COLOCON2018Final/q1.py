# -*- coding:utf-8 -*-
import re
n = int(input())
s = list(map(len, re.split('B+',input())))
a = lambda tmp:(tmp*(tmp+1))//2
if len(s) == 1:
    print(a(s[0]*n))
else:
    ans = 0
    for tmp in s[1:-1]:
        ans += a(tmp)*n
    else:
        ans += a(s[0])+a(s[-1])+a(s[0]+s[-1])*(n-1)
    print(ans)
'''
# O(len(s)*n)
positionB = []
ans = 0
check = list(set(s))
if 'A' not in check:
    print(ans)
elif 'B' not in check:
    for positionNum in range(1,len(s)+1):
        for line in range(n):
            ans += positionNum+len(s)*line
    print(ans)
else:
    for index, factor in enumerate(s):
        if factor == 'B':
            for line in range(n):
                positionB.append((index+1)+len(s)*line)
        else:
            pass
    else:
        positionB.sort()
        for index in range(0, len(positionB)-1):
            length = positionB[index+1]-positionB[index]-1
            if length:
                ans += sum([tmp for tmp in range(1,length+1)])
            else:
                pass
        else:
            ans += sum([tmp for tmp in range(positionB[0]) if tmp != 0])
            ans += sum([tmp for tmp in range(1,len(range(positionB[len(positionB)-1]+1,(len(s)*n)+1))+1) ])
    print(ans)
'''
