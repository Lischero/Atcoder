# -*- coding:utf-8 -*-
import math
N, A = map(int,input().split())
x = [0] + list(map(int,input().split()))
ans = 0
if max(x) < A:
    maximum = A
else:
    maximum = max(x)
#sum/n = A ---> sum = nA
#calc[a][b][c] a番目のカードまで選んでからb枚を抜き出した時、合計がcになる通り。
calc = [[[0 for c in range(N*maximum+1)] for b in range(N+1)] for a in range(N+1)]
for a in range(N+1):
    for b in range(N+1):
        for c in range(N*maximum+1):
            if not a and not b and not c:
                calc[a][b][c] = 1
            elif a >= 1 and b >= 1 and c >= x[a]:
                calc[a][b][c] = calc[a-1][b][c]+calc[a-1][b-1][c-x[a]]
            elif a >= 1 and c < x[a]:
                calc[a][b][c] = calc[a-1][b][c]
            else:
                calc[a][b][c] = 0

for b in range(1,N+1):
    ans += calc[N][b][b*A]
print(ans)
