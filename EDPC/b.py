N,K = map(int,input().split())
H = list(map(int,input().split()))
INF = float('inf')
dp = [INF for _ in range(N)]
dp[0] = 0
for i in range(N):
  for k in range(1,K+1):
    if 0 <= i-k < N:
      dp[i] = min(dp[i],dp[i-k] + abs(H[i]-H[i-k]))
print(dp[N-1])