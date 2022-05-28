N = int(input())
#dp[i][j] = (i日目に行動jをしたときの幸福度の総和の最大値)
dp = [[0,0,0] for _ in range(N+1)]
for i in range(N):
  a,b,c = map(int,input().split())
  if i == 0:
    dp[0][0],dp[0][1],dp[0][2] = a,b,c
  else:
    dp[i][0] = max(dp[i-1][1]+a,dp[i-1][2]+a)
    dp[i][1] = max(dp[i-1][0]+b,dp[i-1][2]+b)
    dp[i][2] = max(dp[i-1][1]+c,dp[i-1][0]+c)
print(max(dp[N-1]))