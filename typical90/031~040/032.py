import itertools
#入力
N = int(input())
A = []
for _ in range(N):
  a = list(map(int,input().split()))
  A.append(a)
M = int(input())
ans = 10**10
discord = [[0 for i in range(N)] for j in range(N)]
#discoed[x][y] = 1なら選手xと選手yは不仲
for _ in range(M):
  X,Y = map(int,input().split())
  discord[X-1][Y-1] = 1
  discord[Y-1][X-1] = 1

#順列を全探索
for v in itertools.permutations(range(N), N):
  time = A[v[0]][0]
  Is_friendly = True #不仲な選手が隣り合っていないか
  for i in range(N-1):
    time += A[v[i+1]][i+1]
    if discord[v[i]][v[i+1]]:
      Is_friendly = False
  if Is_friendly:
      ans = min(ans,time)

#出力
if ans == 10**10:
  print(-1)
else:
  print(ans)