# -*- coding:utf-8 -*-
if __name__ == "__main__":
    a, b = map(int, input().split())
    #等差数列の公式を使う．
    rightLength = (b-a)*(b-a+1)/2
    ans = int(rightLength - b)
    print(ans)
