# -*- coding:utf-8 -*-
import sys
def cell():
    global money, l, x
    money += x.pop(0)
    a = [ tmp for tmp in l if tmp[0] <= money ]
    a.sort(key=lambda x:x[1], reverse=True)
    factor = a.pop(0)
    l.pop(l.index(factor))
    return

def purchase(cost):
    global money, result, l
    money -= cost
    for tmp in target:
        l.pop(0)
        result += tmp[1]
    return

def finish():
    global result
    print(result)
    sys.exit()

if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    c = list(map(int, input().split()))
    v = list(map(int, input().split()))
    l = [ (cost, value) for cost, value in zip(c,v) ]
    result = 0
    money = 0
    while len(l) > 0:
        l.sort(key = lambda x:x[1], reverse=True)
        totalPrice = 0
        target = []
        if min(l, key=lambda x:x[0])[0] > money:
            cell()
        else:
            for tmp in l:
                totalPrice += tmp[0]
                if money < totalPrice:
                    if len(target) == 0:
                        if len(x) == 0:
                            finish()
                        else:
                            cell()
                        break
                    else:
                        purchase(totalPrice-tmp[0])
                        break
                else:
                    target.append(tmp)
            else:
                if len(target) > 0:
                    purchase(totalPrice)
                else:
                    pass
    else:
        finish()
