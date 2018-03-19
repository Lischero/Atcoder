# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    s = [ input() for _ in range(n) ]
    m = int(input())
    t = [ input() for _ in range(m) ]
    factors = list(set(s+t))
    dic = { key: 0 for key in factors}
    ans = float("-inf")
    for word in s:
        dic[word] += 1
    for word in t:
        dic[word] -= 1
    for word in list(set(s+t)):
        ans = max(ans, dic[word])
    else:
        if ans < 0:
            print(0)
        else:
            print(ans)
