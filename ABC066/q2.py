# -*- coding:utf-8 -*-
s = input()
sub = 0
for tmp in reversed(range(1,len(s)-2,2)):
    factor = s[0:tmp+1]
    sub += 2
    if factor[0:int(len(factor)/2)] == factor[int(len(factor)/2):len(factor)]:
        break
    else:
        pass
print(len(s)-sub)
