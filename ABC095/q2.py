# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n, x = map(int, input().split())
    m = [ int(input()) for _ in range(n) ]
    ans = len(m)
    singleWeight = sum(m)
    surplus = x - singleWeight
    if surplus > 0:
        ans += surplus//min(m)
        surplus -= min(m)*(surplus//min(m))
    else:
        pass
    print(ans)
