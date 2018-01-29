# -*- coding:utf-8 -*-
a, b, c, x = (int(input()), int(input()), int(input()), int(input()))
factor = []
for tmp in range(a+1):
    for tmp2 in range(b+1):
        for tmp3 in range(c+1):
            if 500*tmp+100*tmp2+50*tmp3 == x:
                factor.append((tmp,tmp2,tmp3))
print(len(factor))
