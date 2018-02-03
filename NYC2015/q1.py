# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = str(bin(int(input())))[2:]
    if n == ''.join(reversed(n)):
        print("Yes")
    else:
        print("No")
