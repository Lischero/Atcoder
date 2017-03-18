# -*- coding:utf-8 -*-
'''
def search(t, x, i):
    global X
    if x == X:
        return t
    elif x > X:
        ans1 = search(i, x, i+1)
        ans2 = search(i, x-i, i+1)
        return min(ans1, ans2)
    else:
        ans3 = search(i, x+i, i+1)
        return ans3
'''
X = int(input())
p, i = (0,0)
while True:
    p += i
    i += 1
    if p >= X:
        break
print(i-1)
'''
ans = search(0, 0, 1)
print(ans)
'''
