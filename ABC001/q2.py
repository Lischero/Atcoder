# -*- coding:utf-8 -*-
m = int(input())/1000
if m < 0.1:
    print("00")
elif m <= 5:
    m *= 10
    if m < 10:
        print("0"+str(int(m)))
    else:
        print(int(m))
elif m >= 6 and m <= 30:
    print(int(m)+50)
elif m >= 35 and m <= 70:
    print(int((m-30)/5+80))
else:
    print("89")
