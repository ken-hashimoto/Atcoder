N = int(input())
INF = float('inf')
X,Y = map(int,input().split())
dp = [[[INF]*(Y+1) for __ in range(X+1)] for _ in range(N+1)]
#dp[i][j][k] = (i番目までの弁当でたこ焼きをj個、たい焼きをk個食べるときに必要な弁当の最小個数)
dp[0][0][0] = 0
for i in range(N):
  a,b = map(int,input().split())
  for j in range(X+1):
    for k in range(Y+1):
      dp[i+1][j][k] = min(dp[i][j][k],dp[i+1][j][k])
      dp[i+1][min(j+a,X)][min(k+b,Y)] = min(dp[i][j][k]+1,dp[i+1][min(j+a,X)][min(k+b,Y)])
print(-1 if dp[N][X][Y] == INF else dp[N][X][Y])