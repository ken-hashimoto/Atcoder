S = input()
mod = 998244353
N = len(S)
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(i + 1):
        if S[i] in {"(", "?"}:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= mod
        if S[i] in {")", "?"} and j > 0:
            dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j - 1] %= mod

print(dp[N][0] % mod)
