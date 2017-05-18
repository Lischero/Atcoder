# -*- coding:utf-8 -*-
N, K = map(int, input().split())
S = list(input())
a = sorted(S)
b = sorted(S)
T = []
for tmp in range(N): #tmpはTの決定文字番号。
    '''
    check = 0
    for i in range(len(T)):
        if S[i] != T[i]:
            check += 1
        else:
            pass
    '''
    for tmp2 in range(len(a)):
        print("a:"+str(a))
        print("b:"+str(b))
        #a[tmp2]を仮にTに入れる文字だとする。
        c = b.pop(tmp2) #bはb[tmp2]をTに仮に入れた場合の文字列。cはTに入れる文字。
        print("check:"+str(c))
        e = 0
        d = list((''.join(S))[tmp+1:N])
        print("d:"+str(d))
        for tmp3 in list(set(b)):
            f = b.count(tmp3) #残りの文字列内のある文字の個数。
            g = d.count(tmp3) #文字列Sの部分文字列におけるある文字の個数。
            e += min(f,g) #ある文字の数での一致数を格納。
        print("len(d)-e:"+str(len(d)-e))
        if len(d) - e <= K-1:
            K -= len(d)-e
            a.pop(tmp2)
            T.append(c)
            print("T:"+str(T))
            print("a(after pop):"+str(a))
            print("----------------------")
            break
        else:
            b.append(c)
            b.sort()

print(''.join(T))













'''
for tmp in range(N): #tmpはTの決定文字番号。
    a.sort()
    for tmp2 in range(len(a)):
        #a[tmp2]を仮にTに入れる文字だとする。
        c = a.pop(tmp2) #aはa[tmp]をTに仮に入れた場合の文字列。cはTに入れる文字。
        e = 0
        d = list((''.join(S))[tmp+1:N])
        for tmp3 in list(set(a)):
            f = a.count(tmp3) #残りの文字列内のある文字の個数。
            g = d.count(tmp3) #文字列Sの部分文字列におけるある文字の個数。
            e += min(f,g) #ある文字の数での一致数を格納。
        if len(d) - e <= K-1:
            K -= len(d)-e
            T.append(c)
            break
        else:
            a.append(c)
            #a.sort()
'''
