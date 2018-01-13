# -*- coding:utf-8 -*-
class Node:
    def __init__(self,taskNum,taskTime):
        self.taskNum = taskNum
        self.taskTime = taskTime
        self.tasked = []

def insert(node, taskNum, taskTime):
    node.tasked.append(Node(taskNum, taskTime))

def search(node, taskNum):
    for tmp in node.tasked:
        if tmp.taskNum == taskNum:
            return tmp
        else:
            return search(tmp, taskNum)
    else:
        return None #見つからない場合．


N = int(input())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
indexDic = {} #xの中の依存タスク関係を示す．(キー:依存されるタスク番号，要素：xのインデックス番号の配列
for tmp in range(len(a)):
    if a[tmp] in indexDic:
        indexDic[a[tmp]].append(tmp+1)
    else:
        indexDic[a[tmp]] = [tmp+1]

node = Node(1,x[0])

for taskNum in range(1, len(x)+1):
    if taskNum == 1:
        insertedNode = node
    else:
        insertedNode = search(node, taskNum)

    if taskNum in indexDic:
        for indexNumX in indexDic[taskNum]:
            insert(insertedNode, indexNumX+1, x[indexNumX])

