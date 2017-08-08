# -*- coding:utf-8 -*-
N = int(input())
factor = 0
a = list(map(int, input().split()))
b = [ tmp for tmp in a if tmp%4 == 0 ]
c = [ tmp for tmp in a if tmp%2 == 0 ]
d = [ tmp for tmp in a if tmp%2 != 0 ]
if len(c)-len(b) != 0 and len(b)-len(d) >= 0:
    print("Yes")
elif len(c)-len(b) == 0 and len(b)+1 >= len(d):
    print("Yes")
else:
    print("No")
