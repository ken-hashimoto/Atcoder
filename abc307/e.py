N,M = map(int,input().split())
# dp[i] = (i人目までですべての人が異なる数字を持つ方法の数)
same = 0
notSame = 1

MOD = 998244353
dp = [[0]*2 for _ in range(N)]
dp[0][same] = M
dp[0][notSame] = 0
dp[1][same] = 0
dp[1][notSame] = (M*(M-1))%MOD
for i in range(2,N):
    dp[i][same] = dp[i-1][notSame]
    dp[i][same] %= MOD
    dp[i][notSame] = dp[i-1][same]*(M-1) + dp[i-1][notSame]*(M-2)
    dp[i][notSame] %= MOD
print(dp[N-1][notSame]%MOD)