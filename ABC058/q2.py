# -*- coding;utf-8 -*-
O, E = (list(input()),list(input()))
O.reverse()
E.reverse()
factor = len(O)+len(E)
num = 1
ans = []
while factor > 0:
    if num%2 != 0:
        tmp = O.pop()
    else:
        tmp = E.pop()
    ans.append(tmp)
    num += 1
    factor -= 1
ans = ''.join(ans)
print(ans)


