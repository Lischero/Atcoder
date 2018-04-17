# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    x = [ (number, index) for number, index in zip(list(map(int, input().split())),range(n)) ]
    x.sort(key=lambda tmp:tmp[0])
    indexDic = { index[1]: xindex for index, xindex in zip(x,range(n)) }
    center = int(n/2)
    for tmp in range(n):
        ignoreIndex = indexDic[tmp]
        if ignoreIndex+1 <= center:
            print(x[center][0])
        else:
            print(x[center-1][0])
