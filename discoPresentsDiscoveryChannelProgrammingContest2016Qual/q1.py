# -*- coding:utf-8 -*-
w = int(input())
s = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'
for tmp in range(0, len(s), w):
    print(s[tmp:tmp+w])
