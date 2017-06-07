# -*- coding:utf-8 -*-
import sys
N, K = map(int, input().split())
s = sorted([ int(input()) for tmp in range(N) ])
a = list(filter(lambda n:n<=K, s))
if len(a) != 0:
    if 0 in s:
        print(len(s))
        sys.exit()
    else:
        b = list(filter(lambda n:n!=1, a))
        ans = len(a)-len(b)
        c = 0
        right = 0
        d = 1
        for left in range(len(b)):
            while right < len(b) and d*b[right] <= K:
                if right < left:
                    right -= 1
                    break
                d *= b[right]
                right += 1
            d /= b[left]
            if c < right-left:
                c = right-left
        print(ans+c)
else:
    print(0)
