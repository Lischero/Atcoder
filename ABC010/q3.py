# -*- coding:utf-8 -*-
import math, sys
tx_a, ty_a, tx_b, ty_b, T, V = map(int, input().split())
n = int(input())
total_distance, coordinate  = ( V*T, [] )
for tmp in range(n):
    x, y = map(int, input().split())
    coordinate.append((x,y))
for tmp in range(n):
    tmp2 = math.sqrt(((coordinate[tmp])[0] - tx_a)**2 + ((coordinate[tmp])[1] - ty_a)**2)
    tmp3 = math.sqrt((tx_b-(coordinate[tmp])[0])**2 + (ty_b - (coordinate[tmp])[1])**2)
    distance = tmp2+tmp3
    if distance <= total_distance:
        print("YES")
        sys.exit()
    else:
        pass
print("NO")
