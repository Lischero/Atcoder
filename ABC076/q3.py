# -*- coding:utf-8 -*-
import re, itertools
s = list(input())
t = input()
alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
index = [ tmp for tmp in range(len(s)) if s[tmp] == '?' ]
num = len(index)
factor = []
if num:
    a = itertools.combinations_with_replacement(alphabet, num)
    #a = itertools.combinations_with_replacement(list(set(t)), num)
    for b in a:
        sentence = []
        trans = list(reversed(b))
        for c in s:
            if c == '?':
                sentence.append(trans.pop())
            else:
                sentence.append(c)
        factor.append(''.join(sentence))
    factor.sort()
    #print(factor)
    ans = [ tmp for tmp in factor if len(re.findall(r'%s'%t,tmp)) > 0 ]
    if len(ans) > 0:
        print(ans[0])
    else:
        print("UNRESTORABLE")
else:
    if len(re.findall(r'%s'%t, ''.join(s))) > 0:
        print(''.join(s))
    else:
        print("UNRESTORABLE")
