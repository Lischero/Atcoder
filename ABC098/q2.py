# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    s = input()
    ans = float('-inf')
    for end in range(1,n):
        ans = max(ans, len([tmp for tmp in list(set(s[0:end])) if list(set(s[end:n])).count(tmp) > 0]))
    else:
        print(ans)
