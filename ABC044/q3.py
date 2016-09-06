# -*- coding: utf-8 -*-
#まだ回答途中。
N,A = list(map(int,input().split()));
x = list(map(int,input().split()));
answer = 0

for i in range(len(x)): #平均と同じ数字のみ選んだ場合。
	if(x[i] == A):
		answer += 1

print(answer)
