# -*- coding:utf-8 -*-
S = list(input())
if S[2] == 'B':
    print("Bachelor "+''.join(S[0:2]))
elif S[2] == 'M':
    print("Master "+''.join(S[0:2]))
else:
    print("Doctor "+''.join(S[0:2]))
