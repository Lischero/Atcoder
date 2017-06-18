# -*- coding:utf-8 -*-
S = list(input())
flag1 = True 
flag2 = True
list1 = [ tmp for tmp in S if tmp == 'N' or tmp == 'S' ]
list2 = [ tmp for tmp in S if tmp == 'W' or tmp == 'E' ]
if len(list1) > 0:
    if 'N' in list1 and 'S' in list1:
        pass
    else:
        flag1 = False
if len(list2) > 0:
    if 'W' in list2 and 'E' in list2:
        pass
    else:
        flag2 = False
if flag1 and flag2:
    print("Yes")
else:
    print("No")
