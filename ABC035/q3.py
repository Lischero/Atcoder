# -*- coding: utf-8 -*-

NQ = list(map(int, input().split()))
s = [0] * NQ[0]
counter = 0
while counter < NQ[1]:
	lr = list(map(int, input().split()))
	s[ lr[0] - 1 ] += 1
	if lr[1] < NQ[0]:
		s[ lr[1] ] -= 1 #差分修正用。
	counter += 1
else:
	counter = 0

while counter < NQ[0] - 1:
	s[counter+1] = s[counter]+s[counter+1] #累積和を生成。
	counter += 1

#終了段階で偶数だったら黒、奇数なら白？
for i in range(0,NQ[0]):
	s[i] = s[i]%2
else:
	ans = list(map(str,s))
	print(''.join(ans))
			
			
	

		


