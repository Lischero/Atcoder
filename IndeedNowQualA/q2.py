# -*- coding:utf-8 -*-
N = int(input())
keyword = list('indeednow')
nums = []
result = [ True for tmp in range(N) ]
factor = list(sorted(set(keyword), key=keyword.index))
for tmp in factor:
    nums.append(keyword.count(tmp))

for tmp in range(N):
    s = list(input())
    if len(s) != len(keyword):
        result[tmp] = False
    else:
        for tmp2 in range(len(factor)):
            if s.count(factor[tmp2]) != nums[tmp2]:
                result[tmp] = False
                break

for tmp in range(N):
    if result[tmp]:
        print("YES")
    else:
        print("NO")
