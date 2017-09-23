# -*- coding:utf-8 -*-
n, m, k = map(int, input().split())
factor = []
factor.append(n*m)
#for tmp in range(min(n,m)):
#    sides = tmp+1
#    factor.append(sides**2+((n-sides)*(m-sides)))
factor.append((n//2)*(m//2)*2 + ((((n%2)*m+(m%2)*n)-1)//2 + 1))
for tmp in range(1,n+1):
    for tmp2 in range(1, m+1):
        factor.append(tmp*tmp2 + (n-tmp)*(m-tmp2))
factor = list(set(factor))
if k in factor or k%n == 0 or k%m == 0:
    print("Yes")
else:
    print("No")
