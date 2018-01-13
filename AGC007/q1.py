# -*- coding:utf-8 -*-
def search(y, x):
    global h, w, a
    if y >= h or x >= w:
        return False

    if y == h-1 and x == w-1:
        return True

    if a[y][x] == '.':
        return False
    else:
        return search(y+1, x) or search(y, x+1)

if __name__ == "__main__":
    h, w = map(int, input().split())
    a = [ list(input()) for y in range(h) ]
    print("Possible" if search(0,0) else "Impossible")
