# -*- coding:utf-8 -*-
import sys
s = list(input())
t = list(input())
sentence = s*2
for tmp in range(len(s)):
    index = len(s)-tmp
    if ''.join(t) == ''.join(sentence[index:index+len(s)]):
        print(tmp)
        sys.exit()
    else:
        pass
else:
    print(-1)
