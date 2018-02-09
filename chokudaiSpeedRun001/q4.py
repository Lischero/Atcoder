# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n = int(input())
    print(' '.join(list(map(str, list(sorted(list(map(int, input().split()))))))))
