import itertools
import operator
N,K = map(int,input().split())
A = list(map(int,input().split()))
MOD = 10**9 + 7
#dp[i][j] = (i番目までの子どもたちでj個の飴を分けるときの場合の数)
#求めるのはdp[N][K]
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
  s = list(itertools.accumulate(dp[i-1]))
  #s[i] = dp[i-1][0] + ... + dp[i-1][i]
  for j in range(K+1):
    a = A[i-1]
    #dp[i][j] = dp[i-1][j] + ... dp[i-1][j-a]
    dp[i][j] = s[j]
    if j-a-1 >= 0:
      dp[i][j] -= s[j-a-1]
    dp[i][j] %= MOD
print(dp[N][K])