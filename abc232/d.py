from collections import deque

H,W = map(int,input().split())
G = [list(input()) for _ in range(H)]
dist = [[-1]*W for _ in range(H)]
d = deque()
d.append((0,0))
dist[0][0] = 1
ans = 1
while d:
  x,y = d.popleft()
  if x+1 <H:
    if G[x+1][y] != "#" and dist[x+1][y] == -1:
      dist[x+1][y] = dist[x][y]+1
      ans = max(dist[x+1][y],ans)
      d.append((x+1,y))
  if y+1 <W:
    if G[x][y+1] != "#" and dist[x][y+1] == -1:
      dist[x][y+1] = dist[x][y]+1
      ans = max(dist[x][y+1],ans)
      d.append((x,y+1))
print(ans)
