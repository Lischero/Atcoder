# -*- coding:utf-8 -*-
s = list(input())
alphabet = [ chr(tmp) for tmp in range(97, 97+26) ]
candinate = []
for tmp1 in alphabet:
    if tmp1 not in s:
        pass
    else:
        sentence = [ a for a in s ]
        ans = 0
        while True:
            if ''.join([tmp1 for tmp3 in range(len(sentence))]) == ''.join(sentence):
                candinate.append(ans)
                break
            for tmp2 in range(len(sentence)-1):
                if sentence[tmp2] == tmp1:
                    pass
                elif sentence[tmp2+1] == tmp1:
                    sentence[tmp2] = sentence[tmp2+1]
                else:
                    pass
            sentence.pop()
            ans += 1
print(min(candinate))
