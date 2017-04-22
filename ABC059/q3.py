# -*- coding:utf-8 -*-
n = int(input())
a = list(map(int, input().split()))

#nega
total = 0
sign = -1
nega_cost = 0
for tmp in range(len(a)):
    total += a[tmp]
    if total * sign <= 0:
        nega_cost += abs(total*sign)+1
        total = sign
    sign *= -1

#posi
total = 0
sign = 1
posi_cost = 0
for tmp in range(len(a)):
    total += a[tmp]
    if total * sign <= 0:
        posi_cost += abs(total*sign)+1
        total = sign
    sign *= -1

print(min(nega_cost, posi_cost))

'''
l = []
even = 0
odd = 0
for tmp in range(1,n+1):
    ans = sum(a[0:tmp])
    l.append(ans)
    if len(l) >= 2 and len(l)%2 == 0:
        if abs(l[len(l)-2]) < abs(l[len(l)-1]):
            odd += 1
        else:
            even += 1
#even > odd
for tmp in range(len(l)):
    if tmp%2 == 0:
        
print(l)
print(odd)
print(even)
'''
