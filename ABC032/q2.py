# -*- coding:utf-8 -*-
s, k = (input(), int(input()))
if len(s) < k:
    print(0)
else:
    l = []
    for tmp in range(len(s)):
        if len(s) == k:
            l.append(s[0:len(s)])
            break
        else:
            l.append(s[tmp:tmp+k])
            if len(l[-1]) < k:
                l.pop()
    ans = len(list(set(l)))
    print(ans)
