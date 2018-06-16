# -*- coding:utf-8 -*-
def check(num):
    if num%2:
        return 0
    else:
        return 1

def process(num):
    if num == 2:
        return num*3
    else:
        return int(num/2)

if __name__ == "__main__":
    n = int(input())
    a = [ tmp for tmp in list(map(int, input().split())) if check(tmp) ]
    ans = 0
    while(len(a)):
        a = [ tmp for tmp in list(map(process, a)) if check(tmp) ]
        ans += 1
    print(ans)
