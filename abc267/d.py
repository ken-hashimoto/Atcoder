N,M = map(int,input().split())
A = list(map(int,input().split()))
#dp[i][l] = (A[:i]における長さlの部分列の問題文のスコアの最大値)
#総和ももっといた方がよい
#dp[N][M]がほしい
INF = float('inf')
dp = [[-INF]*(M+2)  for _ in range(N+2)]
dp[0][0] = 0

for i in range(1,N+1):
  for l in range(1,M+2):
    dp[i][l] = dp[i-1][l]
    if dp[i][l] <= dp[i-1][l-1]  + l * A[i-1]:
      dp[i][l] = dp[i-1][l-1]  + l * A[i-1]
print(dp[N][M])