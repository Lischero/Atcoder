# -*- coding:utf-8 -*-
from collections import Counter
import sys
def maxBy(f, x, y):
    if f(x) > f(y):
        return x
    else:
        return y

table = { ("",""):"" }

def lcs(x,y):
    if (x,y) in table:
        return table[(x,y)] #メモ化使用．
    ans = ""
    if x == "" or y == "":
        ans = ""
    elif x[-1] == y[-1]:
        ans = lcs(x[:-1],y[:-1])+x[-1]
    else:
        ans = maxBy(len, lcs(x[:-1], y), lcs(x, y[:-1]))
    table[(x,y)] = ans #メモ化処理
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [ input() for tmp in range(n) ]

b = Counter(s)
factors = [ s[tmp-1] for tmp in a ]
c = Counter(factors)
ans_list = []

for tmp in factors:
    if b[tmp] != c[tmp]:
        print("-1") #重複候補がある場合，引っかかる可能性がある．
        sys.exit()
    else:
        pass
else:
    if len(factors) > 2:
        ans_list.append(lcs(factors[0], factors[1]))
        for tmp in range(2, len(factors)):
            ans_list.append(lcs(ans_list[tmp-2], factors[tmp]))
        else:
            if ans_list[-1] == "":
                print("-1")
            elif n == k:
                print("")
            else:
                print(ans_list[-1])
    elif len(factors) == 2:
        ans = lcs(factors[0], factors[1])
        if ans == "":
            print("-1")
        else:
            print(ans)
    else:
        print("")
