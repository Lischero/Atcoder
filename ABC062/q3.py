# -*- coding:utf-8 -*-
H, W = map(int, input().split())
factors = []
for h1 in range(1,H):
    subHeight = H-h1
    h2 = subHeight//2
    h3 = subHeight-h2
    w2 = W//2
    w3 = W-w2
    s1 = [ h1*W, h2*W, h3*W ]
    s2 = [ h1*W, subHeight*w2, subHeight*w3 ]
    factors.append(max(s1)-min(s1))
    factors.append(max(s2)-min(s2))

for w1 in range(1,W):
    subWidth = W-w1
    w2 = subWidth//2
    w3 = subWidth-w2
    h2 = H//2
    h3 = H-h2
    s1 = [ H*w1, H*w2, H*w3 ]
    s2 = [ H*w1, h2*subWidth, h3*subWidth ]
    factors.append(max(s1)-min(s1))
    factors.append(max(s2)-min(s2))

print(min(factors))
