#dp[i][j]=(i枚目までを投げて表がj枚でる確率)
N = int(input())
P = [0] + list(map(float,input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][0] = 1 - P[1]
dp[1][1] = P[1]
for i in range(3,N+1,2):
  for j in range(N+1):
    dp[i][j] += dp[i-2][j-2] * P[i-1] * P[i]
    dp[i][j] += dp[i-2][j-1] * (P[i-1] * (1 - P[i]) + (1 - P[i-1]) * P[i])
    dp[i][j] += dp[i-2][j] * (1-P[i-1]) * (1-P[i])
print(sum(dp[N][(N+1)//2 :]))