from collections import deque

def solve(city): #cityからそれぞれの都市までの最短距離を出力
  dist = [0 for _ in range(N+1)]
  seen = [False for _ in range(N+1)]
  todo = deque([])
  todo.append(city)
  seen[city] = True
  while todo:
    v = todo.pop()
    for next_v in graph[v]:
      if seen[next_v]:
        continue
      else:
        todo.append(next_v)
        seen[next_v] = True
        dist[next_v] = dist[v] + 1
  return dist

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
  A,B = map(int,input().split())
  graph[A].append(B)
  graph[B].append(A)
dist_1 = solve(1) #dist[i] = (1から都市iまでの最短距離)
farest_city = dist_1.index(max(dist_1))
dist_f_city = solve(farest_city) #dist_f_city[i] = (farest_cityから都市iまでの最短距離)
print(max(dist_f_city)+1)