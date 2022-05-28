N,W = map(int,input().split())
#dp[i][j] = (i番目までの品物を価値がjになるように選んだときの最小の重さ)
INF = float('inf')
dp = [[INF]*(10**5+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
  w,v = map(int,input().split())
  for j in range(10**5 + 1):
    dp[i][j] = dp[i-1][j]
    if 0 <= j-v <= 10**5+1:
      dp[i][j] = min(dp[i][j],dp[i-1][j-v]+w)
#求めるのはdp[N][j]をjが大きいところから見ていってはじめてW以下となったときのj
for j in range(10**5,-1,-1):
  if dp[N][j] <= W:
    print(j)
    exit()
