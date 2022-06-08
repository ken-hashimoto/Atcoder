import itertools
N,M,K = map(int,input().split())
MAX_N = 1010
MAX_M = 5010
MOD = 998244353
#dp[i][j] = (Aの先頭からi項を決めてi項目がjであるような場合の数)
dp = [[0]*(MAX_M) for _ in range(MAX_N)]
for j in range(1,M+1):
  dp[1][j] = 1
for i in range(2,MAX_N):
  cum = list(itertools.accumulate(dp[i-1]))
  #cum[s] = (dp[i-1][0] + ... +dp[i-1][s])
  for j in range(1,M+1):
    dp[i][j] = cum[max(j-K,0)] + (cum[M] - cum[min(j+K-1,M)])
    #dp[i][j] = dp[i-1][0]+...+dp[i-1][j-K] + dp[i-1][j+K]+...+dp[i-1][M]
    if K == 0:
      #Kが0のときは上の式でdp[i-1][j]が二回可算されてしまうので重複分を引く
      dp[i][j] -= dp[i-1][j]
    dp[i][j] %= MOD
ans = (sum(dp[N][1:M+1]))%MOD
print(ans)
