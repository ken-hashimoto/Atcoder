#dp[i][j][k] = (それぞれのワープをi,j,k回行ったときの移動経路の数)
#最終的には(i+j+k==N)であるdp[][][]の和が答え
from sys import stdin
N,M = map(int, stdin.readline().split())
A,B,C,D,E,F = map(int, stdin.readline().split())
mod = 998244353
block = dict()
ans = 0
for i in range(M):
  x,y = map(int, stdin.readline().split())
  if not x in block.keys():
    block[x] = set()
    block[x].add(y)
  else:
    block[x].add(y)
dp = [[[0]*302 for i in range(302)] for j in range(302)]
dp[0][0][0] = 1
for i in range(301):
  for j in range(301):
    for k in range(301):
      x = A*i + C*j + E*k
      y = B*i + D*j + F*k
      if not x+A in block.keys() or not y + B in block[x+A]:
        dp[i+1][j][k] += dp[i][j][k]
        dp[i+1][j][k] %= mod
      if not x+C in block.keys() or not y+D in block[x+C]:
        dp[i][j+1][k] += dp[i][j][k]
        dp[i][j+1][k] %= mod
      if not x+E in block.keys() or not y+F in block[x+E]:
        dp[i][j][k+1] += dp[i][j][k]
        dp[i][j][k+1] %= mod
      if i+j+k == N:
        ans += dp[i][j][k]
        ans %= mod
print(ans%mod)
      