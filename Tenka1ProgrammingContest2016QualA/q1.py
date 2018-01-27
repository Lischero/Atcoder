# -*- coding:utf-8 -*-
if __name__ == "__main__":
    print(sum([ num for num in range(1, 101) if num%15 != 0 and num%5 != 0 and num%3 != 0 ]))
