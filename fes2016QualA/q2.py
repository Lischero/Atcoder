# -*- coding:utf-8 -*-
N = int(input())
a = list(map(int, input().split()))
b = [ (tmp+1,a[tmp]) for tmp in range(len(a)) if a[a[tmp]-1] == tmp+1 ]
print(len(list(set([ tuple(sorted(tmp)) for tmp in b ]))))
