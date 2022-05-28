N,W = map(int,input().split())
#dp[i][j] = (i番目までの品物を、重さがj以下になるように選んだときの価値の最大値)
#求めるのはdp[N][W]
dp = [[-1]*(W+1) for _ in range(N+1)]

#なにも選んでない場合は0
for j in range(W+1):
  dp[0][j] = 0 

for i in range(1,N+1):
  w,v = map(int,input().split())
  for j in range(W+1):
    dp[i][j] = dp[i-1][j]
    if 0 <= j-w <= W:
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[N][W])
