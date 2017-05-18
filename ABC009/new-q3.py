# -*- coding:utf-8 -*-
def search(length): #格納済みの不一致数を取得する。
    num = 0
    for tmp in range(length):
        if S[tmp] != T[tmp]:
            num += 1
        else:
            pass
    return num

N, K = map(int, input().split())
S = list(input())
a = sorted(S) #まだ、使える文字を格納しておく。
b = sorted(S)
T = []
for tmp in range(N): #tmpはTの決定文字番号。
    print("reset")
    i = []
    for tmp2 in range(len(a)):
        print("a:"+str(a))
        #a[tmp2]を仮にTに入れる文字だとする。
        c = b.pop(tmp2) #bはb[tmp2]をTに仮に入れた場合の文字列。cはTに入れる文字。
        print("check:"+str(c))
        e = 0
        d = list((''.join(S))[tmp+1:N])
        print("b:"+str(b))
        print("d:"+str(d))
        for tmp3 in list(set(b)):
            f = b.count(tmp3) #残りの文字列内のある文字の個数。
            g = d.count(tmp3) #文字列Sの部分文字列におけるある文字の個数。
            e += min(f,g) #ある文字の数での一致数を格納。
        print("len(d)-e:"+str(len(d)-e))
        T.append(a[tmp2]) #試し入れ。
        if T[len(T)-1] != S[len(T)-1]:
            i.append(len(d)-e+1)
        else:
            i.append(len(d)-e)
        T.pop()
        print("i:"+str(i))
        b.append(c)
        b.sort()
    if search(len(T))+i[0] <= K:
        f = a.pop(0)
        b.pop(0)
        T.append(f)
        print("T:"+str(T))
        print("a(after pop):"+str(a))
        print("b(last):"+str(b))
        print("----------------------")
    else:
        f = i.index(min(i))
        #T.pop()
        g = a.pop(f)
        b.pop(f)
        T.append(g)
        print("T:"+str(T))
        print("a(after pop):"+str(a))
        print("b(last):"+str(b))
        print("----------------------")
    '''
    else:
        g = i.index(min(i))
        h = a.pop(g)
        b.pop(g)
        T.append(h)
        print("T:"+str(T))
        print("a(after pop):"+str(a))
        print("b(last):"+str(b))
        print("----------------------")
    '''
print(''.join(T))
