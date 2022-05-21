import pprint
from collections import deque
H,W = map(int,input().split())
r_s,c_s = map(lambda x:int(x)-1,input().split())
r_t,c_t = map(lambda x:int(x)-1,input().split())
TURN_CNT = [[10**9]*W for _ in range(H)]
Grid = []
for i in range(H):
  S = input()
  Grid.append(S)
#求めるのはTURN_CNT[r_t][c_t]
TURN_CNT[r_s][c_s] = 0
que = deque()
que.append((r_s,c_s,'|'))
que.append((r_s,c_s,'-'))
while que:
  i, j, vec = que.popleft()
  for next_i,next_j in ((i+1,j),(i-1,j)):
    if not (0 <= next_i < H and 0 <= next_j < W):
      continue
    if Grid[next_i][next_j] == "#":
      continue
    if vec == '|' and TURN_CNT[next_i][next_j] > TURN_CNT[i][j]:
      TURN_CNT[next_i][next_j] = TURN_CNT[i][j]
      que.appendleft((next_i,next_j,'|'))
    if vec == '-' and TURN_CNT[next_i][next_j] > TURN_CNT[i][j] + 1:
      TURN_CNT[next_i][next_j] = TURN_CNT[i][j] + 1
      que.append((next_i,next_j,'|'))
  for next_i,next_j in ((i,j+1),(i,j-1)):
    if not (0 <= next_i < H and 0 <= next_j < W):
      continue
    if Grid[next_i][next_j] == "#":
      continue
    if vec == '|' and TURN_CNT[next_i][next_j] > TURN_CNT[i][j] + 1:
      TURN_CNT[next_i][next_j] = TURN_CNT[i][j] + 1
      que.append((next_i,next_j,'-'))
    if vec == '-' and TURN_CNT[next_i][next_j] > TURN_CNT[i][j]:
      TURN_CNT[next_i][next_j] = TURN_CNT[i][j]
      que.appendleft((next_i,next_j,'-'))
print(TURN_CNT)
