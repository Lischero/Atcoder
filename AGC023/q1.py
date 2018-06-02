# -*- coding:utf-8 -*-
import math
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    cumulative = [0]
    ans = 0
    for tmp in range(len(a)):
        cumulative.append(cumulative[-1]+a[tmp])
    else:
        factor = list(set(cumulative))
    dic = { tmp: 0 for tmp in factor }
    for tmp in cumulative:
        dic[tmp] += 1
    for tmp in factor:
        if dic[tmp] > 1:
            ans += math.factorial(dic[tmp])/(math.factorial(dic[tmp]-2)*2)
    else:
        print(int(ans))
