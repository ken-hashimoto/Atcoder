from collections import deque
H,W = map(int,input().split())
ans = 0
def search(x,y,s_x,s_y,cnt): #再帰でルートを全探索する（バックトラック）
  global ans
  seen[x][y] = True
  for i,j in [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]:
    if not (0 <= i < H and 0 <= j < W):
      continue
    if i == s_x and j == s_y:
      ans = max(cnt,ans)
      break
    if seen[i][j] or Grid[i][j] == '#':
      continue
    else:
      seen[i][j] = True
      search(i,j,s_x,s_y,cnt+1)
      seen[i][j] = False

Grid = []
start = [] #始点となりうる座標を格納
for i in range(H):
  S = list(input())
  Grid.append(S)
for i in range(H):
  for j in range(W):
    if Grid[i][j] == '.':
      start.append((i,j))
for s in start:
  x,y = s
  seen = [[False]*W for _ in range(H)]
  search(x,y,x,y,1)
if ans <= 3:
  print(-1)
else:
  print(ans)