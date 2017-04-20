# -*- coding:utf-8 -*-
X = input()
for tmp in ['ch','o','k','u']:
    X = X.replace(tmp, '')
if X == '':
    print("YES")
else:
    print("NO")
