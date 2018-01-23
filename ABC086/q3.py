# -*- coding:utf-8 -*-
import math
def euclideanDistance(a, b, c, d):
    return math.sqrt((a-b)**2+(c-d)**2)
if __name__ == "__main__":
    N = int(input())
    dic = {}
    queue = [(0,0)]
    time = 0
    maxTime = float('-inf')
    flag = True
    for tmp in range(N):
        t, x, y = map(int, input().split())
        dic[t] = (x, y)
        maxTime = max(maxTime, t)
    timeList = list(dic.keys())
    timeListIndex = 0
    while time < maxTime and flag:
        time += 1
        factor = []
        for tmp in queue:
            x = tmp[0]
            y = tmp[1]
            if time in dic:
                if dic[time] == (x+1,y) or dic[time] == (x-1,y) or dic[time] == (x,y+1) or dic[time] == (x,y-1):
                    factor.append(dic[time])
            else:
                if timeList[timeListIndex] < time:
                    timeListIndex += 1
                nearTime = timeList[timeListIndex]
                coordinate = dic[nearTime] 
                num1 = euclideanDistance(x-1, coordinate[0], y, coordinate[1])
                num2 = euclideanDistance(x+1, coordinate[0], y, coordinate[1])
                num3 = euclideanDistance(x, coordinate[0], y-1, coordinate[1])
                num4 = euclideanDistance(x, coordinate[0], y+1, coordinate[1])
                minimumNum = min(min(num1, num2), min(num3, num4))
                if minimumNum == num1:
                    factor.append((x-1,y))
                elif minimumNum == num2:
                    factor.append((x+1,y))
                elif minimumNum == num3:
                    factor.append((x,y-1))
                else:
                    factor.append((x,y+1))
        else:
            factor = list(set(factor))

        if time in dic and len(factor) == 0:
            flag = False

        queue = factor
    else:
        if flag:
            print("Yes")
        else:
            print("No")

