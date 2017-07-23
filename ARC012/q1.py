# -*- coding:utf-8 -*-
d = input()
l = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
if d == 'Sunday' or d == 'Saturday':
    print(0)
else:
    print(5-l.index(d))
