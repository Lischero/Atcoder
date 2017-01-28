# -*- coding: utf-8 -*-
x = int(input())
ans = 0
"""
tmp = 0
tmp2 = 0
for i in [6,5,4,3,2,1]:
    tmp = int(x/i)
    if tmp < 0:
        continue
    else:
        ans = tmp
        x -= i*tmp
        tmp2 = i - 1
        break
"""

if x%11 == 0:
    ans = int(x/11)*2
elif x%11 <= 6:  
    ans = int(x/11)*2 + 1
else:
    ans = int(x/11)*2 + 2
    
print(ans)
