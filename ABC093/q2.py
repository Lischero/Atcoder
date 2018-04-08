# -*- coding:utf-8 -*-
if __name__ == "__main__":
    a,b,k = map(int, input().split())
    ans = []
    if b-a+1 >= 2*k:
        for tmp in range(a, a+k):
            ans.append(tmp)
        for tmp in range(b-k+1,b+1):
            ans.append(tmp)
    else:
        for tmp in range(a, b+1):
            ans.append(tmp)
    ans.sort()
    for tmp in ans:
        print(tmp)
    #TLE
    '''
    factors = [ tmp for tmp in range(a, b+1) ]
    ans = list(set(factors[0:k]+factors[-k:]))
    ans.sort()
    for factor in ans:
        print(factor)
    '''
