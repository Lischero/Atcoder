# -*- coding:utf-8 -*-
if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    even = 0
    for factor in a:
        if factor%2 == 0:
            even += 1
        else:
            pass
    else:
        print(3**N-2**even)
