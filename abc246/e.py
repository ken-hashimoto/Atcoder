from collections import deque
#枝狩りBFS
N = int(input())
sx,sy = map(int,input().split())
sx -= 1
sy -= 1
gx,gy = map(int,input().split())
gx -= 1
gy -= 1
G = [list(input()) for _ in range(N)]
d = deque()
d.append((sx,sy))
vec = [(1,1),(1,-1),(-1,1),(-1,-1)]
M = 10**9
dist = [[M]*N for _ in range(N)]
dist[sx][sy] = 0
while d:
  x,y = d.popleft()
  current_dist = dist[x][y]
  for vx,vy in vec:
    nx,ny = x,y
    while True:
      nx,ny = nx+vx,ny+vy
      if nx < 0 or N <= nx or ny < 0 or N <= ny:
        break
      if G[nx][ny] == "#":
        break
      if dist[nx][ny] < current_dist + 1:
        break
      dist[nx][ny] = dist[x][y] + 1
      d.append((nx,ny))
if dist[gx][gy] == M:
  print(-1)
else:
  print(dist[gx][gy])
