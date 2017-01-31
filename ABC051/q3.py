# -*- coding: utf-8 -*-
sx, sy, tx, ty = map(int,input().split())
movelist = ['U','D','L','R']
moved = []
countX = tx - sx
countY = ty - sy
#first movement
for y in range (0, countY):
    moved.append(movelist[0])

for x in range (0, countX):
    moved.append(movelist[3])

#second movement
for y in range (0, countY):
    moved.append(movelist[1])

for x in range (0, countX):
    moved.append(movelist[2])

#third movement

moved.append(movelist[2])

for y in range (0, countY+1):
    moved.append(movelist[0])

for x in range (0, countX+1):
    moved.append(movelist[3])

moved.append(movelist[1])

#fourth movement
moved.append(movelist[3])

for y in range (0,countY+1):
    moved.append(movelist[1])

for x in range (0, countX+1):
    moved.append(movelist[2])

moved.append(movelist[0])

print("".join(moved))
