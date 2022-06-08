N,M,K = map(int,input().split())
#dp[i][j] = (1以上M以下の数字からなり、かつ総和がjを超えない長さiの数列の個数)
MOD = 998244353
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(K+1):
  dp[0][i] = 1
#求めるのはdp[N][K]
for i in range(1,N+1):
  for j in range(K+1):
    for k in range(1,M+1):
      if j-k >= 0:
        dp[i][j] += dp[i-1][j-k]
        dp[i][j] %= MOD
print(dp[N][K])