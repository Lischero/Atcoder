# -*- coding:utf-8 -*-
n, a, b, c = (int(input()), int(input()), int(input()), int(input()))
l = [a,b,c]
count, ans, objectNum, s = ( -1, 0, 0,  [] )
while objectNum < n:
    if count%2 == 0 and count != 0:
        l.append(s.pop(0))
    else:
        count += 1
    l = sorted(l)
    factor = l.pop()
    objectNum += factor
    ans += 1
    s.append(factor)
print(ans)
