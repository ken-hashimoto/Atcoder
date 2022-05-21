import sys
from collections import deque
input = sys.stdin.readline
#入力
H,W = map(int,input().split())
r_s,c_s = [int(t) - 1 for t in input().split()]
r_t,c_t = [int(t) - 1 for t in input().split()]
TURN_CNT = [[[10**6+1]*4 for j in range(W)] for k in range(H)]
Grid = [input() for _ in range(H)]
#01BFS
que = deque()
for i in range(4):
  TURN_CNT[r_s][c_s][i] = 0
  que.append((r_s,c_s,i))
dx = (1,-1,0,0)
dy = (0,0,1,-1)
while que:
  i, j, v = que.popleft() #vは今向いている方向
  ni = i + dx[v]
  nj = j + dy[v]
  if (not (0 <= ni < H and 0 <= nj < W)) or Grid[ni][nj] == '#':
    continue
  if TURN_CNT[ni][nj][v] > TURN_CNT[i][j][v]:
    TURN_CNT[ni][nj][v] = TURN_CNT[i][j][v]
    que.appendleft((ni,nj,v)) #コスト0なら先頭に
  for nv in range(4): #方向転換について
    if TURN_CNT[ni][nj][nv] > TURN_CNT[ni][nj][v] + 1:
      TURN_CNT[ni][nj][nv] = TURN_CNT[ni][nj][v] + 1
      que.append((ni,nj,nv)) #コストが増えるなら末尾に
#出力
#min(ans[r_t][c_t])よりこっちの方が高速らしい
ans = 10**7
for i in range(4):
  if ans > TURN_CNT[r_t][c_t][i]:
    ans = TURN_CNT[r_t][c_t][i]
print(ans)
