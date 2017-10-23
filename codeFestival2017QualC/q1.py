# -*- coding:utf-8 -*-
import sys
S = input()
for tmp in range(len(S)-1):
    if S[tmp:tmp+2] == 'AC':
        print("Yes")
        sys.exit()
print("No")
