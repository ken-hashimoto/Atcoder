#dp[i][j]=(S[0:i]でatcoder[0:j]を作る方法が何通りあるか)
#求めたいのはdp[N][7]
N = int(input())
S = '*' + input()
T = '+atcoder'
mod = 10**9 + 7
dp = [[0 for _ in range(8)] for __ in range(N+1)]
dp[0][0] = 1
for i in range(N+1):
  for j in range(7+1):
    if i == 0:
      continue
    dp[i][j] = dp[i-1][j]
    if T[j] == S[i]:
      dp[i][j] += dp[i-1][j-1]
      dp[i][j] %= mod
print(dp[N][7])
