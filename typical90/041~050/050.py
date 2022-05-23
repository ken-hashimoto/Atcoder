N,L =map(int,input().split())
MOD = 10**9 + 7
#dp[i] = (i段目にたどりつく階段ののぼり方の総数)
dp = [0 for _ in range(N+1)]
dp[0] = 1
for i in range(1,N+1):
  dp[i] += dp[i-1]%MOD
  if i-L >= 0:
    dp[i] += dp[i-L]%MOD
print(dp[N]%MOD)