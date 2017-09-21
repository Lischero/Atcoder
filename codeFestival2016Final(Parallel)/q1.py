# -*- coding:utf-8 -*-
import sys
H, W = map(int, input().split())
word = { key:chr(key+65) for key in range(W) }
S = [ list(input().split()) for _ in range(H) ]
for h in range(H):
    for w in range(W):
        if S[h][w] == 'snuke':
            print(str(word[w])+str(h+1))
            sys.exit()
        else:
            pass
