# -*- coding:utf-8 -*-
a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
result = [ 'x' for _ in range(10) ]
ans = []
for num in p:
    if num:
        result[num-1] = '.'
    else:
        result[9] = '.'
for num in q:
    if num:
        result[num-1] = 'o'
    else:
        result[9] = 'o'

print(' '.join(result[6:10]))
print(' '+' '.join(result[3:6]))
print(' '*2+' '.join(result[1:3]))
print(' '*3+result[0])
