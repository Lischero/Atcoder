# -*- coding:utf-8 -*-
import sys
N, K = map(int, input().split())
s = [ int(input()) for tmp in range(N) ]
if len(list(filter(lambda n:n<=K, s))) != 0:
    if 0 in s:
        print(len(s))
        sys.exit()
    else:
        ans = 0
        right = 0
        b = 1
        for left in range(len(s)):
            if right < left:
                right = left
            while right < len(s) and b*s[right] <= K:
                b *= s[right]
                right += 1
            if left != right:
                b /= s[left]
            if ans < right-left:
                ans = right-left
        print(ans)
else:
    print(0)
