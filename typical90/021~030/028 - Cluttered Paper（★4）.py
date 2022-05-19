N = int(input())
M = 10**3 + 1
Grid = [[0 for i in range(M)] for j in range(M)]
for i in range(N):
  lx,ly,rx,ry = map(int,input().split())
  Grid[lx][ly] += 1
  Grid[rx][ry] += 1
  Grid[rx][ly] -= 1
  Grid[lx][ry] -= 1
for i in range(1,M):
  for j in range(M):
    Grid[i][j] += Grid[i-1][j]
for i in range(M):
  for j in range(1,M):
    Grid[i][j] += Grid[i][j-1]
ans_li = [0 for i in range(N+1)]
for i in range(M):
  for j in range(M):
    ans_li[Grid[i][j]] += 1
for ans in ans_li[1:]:
  print(ans)