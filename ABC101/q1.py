# -*- coding:utf-8 -*-
if __name__ == "__main__":
    s = list(input());
    n = 0
    for tmp in s:
        if tmp == '+':
            n += 1
        else:
            n -= 1
    else:
        print(n);
