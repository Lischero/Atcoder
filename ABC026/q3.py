# -*- coding:utf-8 -*-
N = int(input())
B = []
for tmp in range(N+1):
    if tmp != 0 and tmp != 1:
        B.append(int(input()))
    else:
        B.append(0)
asistant = [() for tmp in range(N+1)]
pay = [0 for tmp in range(N+1)]
for factor in range(1,N+1):
    tmp = [i for i,x in enumerate(B) if x == factor]
    asistant[factor] = asistant[factor]+tuple(tmp)
num = N
while num >= 1:
    if len(asistant[num]) == 0:
        pay[num] = 1
    else:
        maximum = -1
        minimum = pay[asistant[num][0]]
        for tmp in range(len(asistant[num])):
            maximum = max(maximum, pay[asistant[num][tmp]])
            minimum = min(minimum, pay[asistant[num][tmp]])
        pay[num] = maximum+minimum+1
    num -= 1
print(pay[1])
