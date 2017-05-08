# -*- coding:utf-8 -*-
import math
deg, dis = map(int,input().split())
deg /= 10
dis = math.floor((dis/60)*10+0.5)/10
Dir, W = ('N', 0)
deglist = [ 33.75, 56.25, 78.75, 101.25, 123.75, 146.25, 168.75,
191.25, 213.75, 236.25, 258.75, 281.25, 303.75, 326.25, 348.75 ]
dirlist = [ "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW" ]
velocity = [ 0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6 ]
for tmp in range(len(velocity)):
    if tmp == 0:
        if 0 <= dis and dis <= velocity[tmp]:
            W = tmp
            break
    else:
        if (velocity[tmp-1]*10+1)/10 <= dis and dis <= velocity[tmp]:
            W = tmp
            break
        if tmp == len(velocity)-1 and (velocity[tmp]*10+1)/10 <= dis:
            W = tmp+1
            break

if W != 0:
    for tmp in range(len(deglist)):
        if tmp == 0:
            if 11.25 <= deg and deg < deglist[tmp]:
                Dir = dirlist[tmp]
                break
        else:
            if deglist[tmp-1] <= deg and deg < deglist[tmp]:
                Dir = dirlist[tmp]
                break
else:
    Dir = 'C'
print(Dir+' '+str(W))
