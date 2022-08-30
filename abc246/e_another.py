from collections import deque
#01BFS
N = int(input())
sx,sy = map(int,input().split())
sx -= 1
sy -= 1
gx,gy = map(int,input().split())
gx -= 1
gy -= 1
G = [list(input()) for _ in range(N)]
d = deque()
M = 10**9
dist = [[[M]*4 for __ in range(N)] for _ in range(N)]
for i in range(4):
  d.append((sx,sy,i,1))
  dist[sx][sy][i] = 1
vec = [(1,1),(1,-1),(-1,1),(-1,-1)]
while d:
  x,y,v,cost = d.popleft()
  if cost > dist[x][y][v]:
    continue
  for i in range(4):
    dx,dy = vec[i]
    nx = x + dx
    ny = y + dy
    if nx < 0 or N <= nx or ny < 0 or N <= ny:
      continue
    if G[nx][ny] == "#":
      continue
    if i == v:
      if cost < dist[nx][ny][i]:
        dist[nx][ny][i] = cost
        d.appendleft((nx,ny,i,cost))
        continue
    else:
      if cost + 1 < dist[nx][ny][i]:
        dist[nx][ny][i] = cost + 1
        d.append((nx,ny,i,cost+1))
        continue
ans = min(dist[gx][gy])
if ans == M:
  print(-1)
else:
  print(ans)