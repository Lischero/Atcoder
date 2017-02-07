# -*- coding: utf-8 -*-
N, K, X, Y = (int(input()), int(input()), int(input()), int(input()))
answer = 0
counter = 1
while counter <= N:
    if(counter <= K):
        answer += X
    else:
        answer += Y
    counter += 1
print (answer)
