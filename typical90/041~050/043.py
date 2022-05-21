#--------------------------------------------------------------
# input here
import sys
import io

_INPUT = """\
3 3
1 1
3 3
..#
#.#
#..

"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
import pprint
from collections import deque
H,W = map(int,input().split())
r_s,c_s = map(int,input().split())
r_t,c_t = map(int,input().split())
TURN_CNT = [[10**9]*(W+1) for _ in range(H+1)]
Grid = ['*'*W]
for i in range(H):
  S = '*' + input()
  Grid.append(S)
#求めるのはTURN_CNT[r_t][c_t]
TURN_CNT[r_s][c_s] = 0
que = deque()
que.append((r_s,c_s,'|'))
que.append((r_s,c_s,'-'))
while que:
  i, j, vec = que.popleft()
  for next_i,next_j in ((i+1,j),(i-1,j)):
    if not (1 <= next_i <= H and 1 <= next_j <= W):
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
    if not (1 <= next_i <= H and 1 <= next_j <= W):
      continue
    if Grid[next_i][next_j] == "#":
      continue
    if vec == '|' and TURN_CNT[next_i][next_j] > TURN_CNT[i][j] + 1:
      TURN_CNT[next_i][next_j] = TURN_CNT[i][j] + 1
      que.append((next_i,next_j,'-'))
    if vec == '-' and TURN_CNT[next_i][next_j] > TURN_CNT[i][j]:
      TURN_CNT[next_i][next_j] = TURN_CNT[i][j]
      que.appendleft((next_i,next_j,'-'))
print(TURN_CNT[r_t][c_t])
