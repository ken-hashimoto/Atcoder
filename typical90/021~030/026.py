from collections import deque
N = int(input())
Graph = [[] for _ in range(N+1)]
for i in range(N-1):
  A,B = map(int,input().split())
  Graph[A].append(B)
  Graph[B].append(A)
todo = deque()
Color = [-1 for _ in range(N+1)]
todo.append(1)
Color[1] = 1
while todo:
  v = todo.popleft()
  for next_v in Graph[v]:
    if Color[next_v] != -1:
      continue
    todo.append(next_v)
    Color[next_v] = (Color[v] + 1)%2
Black = []
White = []
for i in range(1,N+1):
  if Color[i] == 0:
    Black.append(i)
  else:
    White.append(i)
if len(Black) >= len(White):
  print(*Black[:N//2])
else:
  print(*White[:N//2])