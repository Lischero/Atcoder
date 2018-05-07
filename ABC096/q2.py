# -*- coding:utf-8 -*-
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    ans = 0
    for tmp in nums:
        ans += tmp
    ans += max(nums)*((2**k)-1)
    print(ans)
