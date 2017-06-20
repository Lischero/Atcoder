# -*- coding:utf-8 -*-
X = list(input())
stack = []
for tmp in X:
    if tmp == 'T' and (len(stack) == 0 or stack[len(stack)-1] == 'T'):
        stack.append(tmp)
    elif tmp == 'T' and stack[len(stack)-1] == 'S':
        stack.pop()
    else:
        stack.append(tmp)
print(len(stack))
