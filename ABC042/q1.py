# -*- coding:utf-8 -*-
ABC = list(map(int,input().split()))
five = ABC.count(5)
seven = ABC.count(7)
if five == 2 and seven == 1:
    print("YES")
else:
    print("NO")
