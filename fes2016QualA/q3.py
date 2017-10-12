# -*- coding:utf-8 -*-
s = list(input())
k = int(input())
for tmp in range(len(s)):
    if k == 0:
        break
    a = 26-(ord(s[tmp]) - ord('a'))
    if s[tmp] != 'a' and k >= a: 
        k -= a
        s[tmp] = 'a'
    else:
        pass
if k > 0:
    s[len(s)-1] = chr((ord(s[len(s)-1])+k%26))
print(''.join(s))
