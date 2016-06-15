# -*- coding:utf-8 -*-
factor = list(map(int, input().split()))
answer = 2 * (factor[0] * factor[1] + factor[0] * factor[2] + factor[1] * factor[2])
print(answer)
