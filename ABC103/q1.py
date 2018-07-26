# -*- coding:utf-8 -*-
import itertools
if __name__ == "__main__":
    a  = list(map(int, input().split()))
    ans = float('inf')
    factor = list(itertools.permutations(a))
    for tuples in factor:
        cost = 0
        for tmp in range(1,3):
            cost += abs(tuples[tmp]-tuples[tmp-1])
        ans = min(ans, cost)
    print(ans)
