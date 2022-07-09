from collections import deque


N = int(input())
X = [[] for _ in range(250)]
for i in range(N):
  a,b = map(int,input().split())
  X[a].append(b,'red')
for i in range(N):
  c,d = map(int,input().split())
  X[c].append(d,'blue')

wait = []
for i in range(1,250):
  for item in X[i]:
    if item[1] == 'red':
      wait.append(item[0])
    