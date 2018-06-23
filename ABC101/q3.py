# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    minimumNum = min(a)
    placeIndex = []
    distance = []
    countIndex = 0
    ans = 0

    #最小値がある場所のインデックスを取得。
    for tmp in a:
        if tmp == minimumNum:
            placeIndex.append(countIndex)
        countIndex += 1

    #配列開始地点から最初の最小値の位置までの要素数
    if placeIndex[0] > 0:
        distance.append(placeIndex[0])

    #placeIndex[tmp]を含まず、次のplaceIndex[tmp+1]を含む要素数
    for tmp in range(len(placeIndex)-1):
        distance.append(abs(placeIndex[tmp]-placeIndex[tmp+1])-1)

    #最後の最小値出現地点から配列a末尾までの要素数
    if placeIndex[-1] != len(a)-1:
        distance.append(len(a)-1-placeIndex[-1])

    if len(placeIndex) == 1 and placeIndex[0] == 0:
        distance.append(len(a)-1)

    index = 0
    base = 0
    while(index < len(distance)):
        base += distance[index]
        if base >= k:
            distance[index] -= base-k
            base = 0
            ans += 2
        else:
            distance[index] = 0

        if distance[index] == 0:
            index += 1
    else:
        if base > 0:
            ans += 1

    print(ans)




