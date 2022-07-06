#dp[i][j] = (S[:i]までで"chokudai"のj文字目までをつくる方法は何通りあるか)
S = input()
N = len(S)
S = '*' + S
T = '+chokudai'
mod = 10**9 + 7
dp = [[0 for _ in range(8+1)] for __ in range(N+1)]
dp[0][0] = 1
for i in range(N+1):
  for j in range(8+1):
    if i == 0:
      continue
    dp[i][j] = dp[i-1][j]
    if T[j] == S[i]:
      dp[i][j] += dp[i-1][j-1]
      dp[i][j] %= mod
print(dp[N][8])