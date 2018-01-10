# -*- coding:utf-8 -*-
def isPrime(num):
    a = 2
    if num == 1:
        return False

    while num >= a*a:
        if num%a == 0:
            return False
        a += 1

    return True

if __name__ == '__main__':
    q = int(input())
    a = []
    b = {}
    c = []
    for tmp in range(q):
        l, r = map(int, input().split())
        a.append((l,r))

    for tmp in range(1, (10**5)+1):
        factor = (tmp+1)/2
        if isPrime(tmp) and factor == int(factor) and isPrime(factor):
            b[tmp] = 1
        else:
            b[tmp] = 0
    
    c.append(b[1])
    for tmp in range(2,(10**5)+1):
        if b[tmp]:
            c.append(c[len(c)-1]+1)
        else:
            c.append(c[len(c)-1])

    for tmp in a:
        threshold = tmp[0]-2
        if threshold < 0:
            print(c[tmp[1]-1])
        else:
            print(c[tmp[1]-1]-c[threshold])

    '''
    for tmp in a:
        ans = 0
        for tmp2 in range(tmp[0], tmp[1]+1):
            if b[tmp2] == 1:
                ans += 1
        print(ans)
    '''
