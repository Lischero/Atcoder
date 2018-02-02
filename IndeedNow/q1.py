# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    highFactors = a[0:n//2]
    lowFactors = sorted(a[n//2:n])
    ansFactors = [ highFactors[tmp]+lowFactors[tmp] for tmp in range(len(highFactors)) ]
    ansFactors.sort()
    print(ansFactors[-1] - ansFactors[0])
