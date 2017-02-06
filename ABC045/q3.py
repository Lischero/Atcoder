# -*- coding:utf-8 -*-
from decimal import *
def sum(sentence):
    if len(sentence) != 0:
        num = int(sentence)
    else:
        num = 0
    for tmp in range (1, len(sentence)):
        num += Decimal(int(sentence[0:tmp])) * Decimal(pow(2, (len(sentence)-tmp-1)))
        print("1."+str(num))
        sentence = sentence[tmp:len(sentence)]
        num += Decimal(int(sum(sentence)))
        print("2."+str(num))
    return num

S = input()
ans = sum(S)
print(ans)
