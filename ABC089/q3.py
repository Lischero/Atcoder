# -*- coding:utf-8 -*-
import sys
if __name__ == "__main__":
    n = int(input())
    s = [ input() for tmp in range(n) ]
    alphabetDic = { alphabet : 0 for alphabet in [ chr(tmp) for tmp in range(ord('A'), ord('A')+26) ] }
    ans = 0
    for word in s:
        alphabetDic[word[0]] += 1
    factors = [ alphabetDic[tmp] for tmp in ['M', 'A', 'R', 'C', 'H'] if alphabetDic[tmp] > 0 ]
    if len(factors) <= 2:
        print(ans)
        sys.exit()
    for tmp in range(len(factors)):
        for tmp2 in range(tmp+1, len(factors)):
            for tmp3 in range(tmp2+1, len(factors)):
                ans += factors[tmp]*factors[tmp2]*factors[tmp3]
    else:
        print(ans)
