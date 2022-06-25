import math
from collections import deque


INF = float('inf')
def calc(x1,y1,x2,y2,p):
  return (abs(x1-x2) + abs(y1-y2))/p
N = int(input())
cost = [[INF]*N for _ in range(N)]
#cost[i][j] = (iからjまでいくときの最小コスト)としたい
#そのためにワーシャルフロイド法を用いる
for i in range(N):
  cost[i][i] = 0
zahyou = []
for _ in range(N):
  x,y,p = map(int,input().split())
  zahyou.append([x,y,p])
for i in range(N):
  x1,y1,p1 = zahyou[i]
  for j in range(N):
    if i == j:
      continue
    x2,y2,p2 = zahyou[j]
    d = math.ceil(calc(x1,y1,x2,y2,p1))
    cost[i][j] = d #辺を張る
#ここからワーシャルフロイド法---------------------------------
for k in range(N):
  for i in range(N):
    for j in range(N):
      if cost[i][k] != INF and cost[k][j] != INF:
        cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
#------------------------------------------------------------

#コストがX以下のとこだけを通って全ての頂点にいけるかを考える
#答えの決め打ちの二分探索

left = 0         #全ての頂点にいけない
right = 10**18   #全ての頂点にいける 
while left + 1 != right:
  mid = (left+right)//2 #コストがmid以下のとこだけを通って全ての頂点にいけるか
  for i in range(N): #始点iを決める
    seen = [False]*N
    seen[i] = True
    todo = deque()
    todo.append(i)
    while todo:
      v = todo.pop()
      for j in range(N):
        if j == v:
          continue
        if seen[j]:
          continue
        if cost[v][j] <= mid:
          seen[j] = True
          todo.append(j)
    #始点iから全ての頂点をたどれるかをみる
    ok_flag = True
    for j in range(N):
      if seen[j] == False:
        ok_flag = False
        break
    if ok_flag: #たどれる場合
      right = mid
      break
    if i == N-1:#たどれなかったとき
      left = mid
print(right)
