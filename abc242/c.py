N = int(input())
MOD = 998244353
dp = [[0]*10 for _ in range(N)]
for i in range(N):
  for j in range(1,10):
    if i == 0:
      dp[i][j] = 1
      continue
    if j == 1:
      dp[i][j] = dp[i-1][2] + dp[i-1][1]
    elif j == 9:
      dp[i][j] = dp[i-1][9] + dp[i-1][8]
    else:
      dp[i][j] = dp[i-1][j+1] + dp[i-1][j]+ dp[i-1][j-1]

print(sum(dp[N-1])%MOD)
