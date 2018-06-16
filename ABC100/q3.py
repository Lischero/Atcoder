# -*- coding:utf-8 -*-
def check(num):
    if num%2:
        return 0
    else:
        return 1

def process(num):
    count = 0
    while(num%2 == 0):
        num //= 2
        count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    a = list(map(process, [ tmp for tmp in list(map(int, input().split())) if check(tmp) ]))
    ans = sum(a)
    print(ans)
