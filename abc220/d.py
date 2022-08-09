N = int(input())
A = list(map(int,input().split()))
mod = 998244353
#dp[i][j] = i回操作を行ったときの第1項目がjであるような操作の数
dp = [[0]*10 for _ in range(N+10)]
#求めるのはdp[N-1][K]
dp[0][A[0]] = 1
for i in range(N-1):
  for j in range(10):
    dp[i+1][(j+A[i+1])%10] += dp[i][j]
    dp[i+1][(j*A[i+1])%10] += dp[i][j]
    dp[i+1][(j+A[i+1])%10] %= mod
    dp[i+1][(j*A[i+1])%10] %= mod
for k in range(10):
  print(dp[N-1][k]%mod)