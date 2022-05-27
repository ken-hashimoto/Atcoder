N = int(input())
H = list(map(int,input().split()))
dp = [0 for _ in range(N)]
#dp[i] = (足場iにたどり着くのに必要な最小コスト)
dp[0] = 0 #0-indexed
for i in range(1,N):
  if i == 1:
    dp[i] = dp[i-1] + abs(H[i]-H[i-1])
  else:
    dp[i] = min(dp[i-1] + abs(H[i]-H[i-1]),dp[i-2] + abs(H[i]-H[i-2]))
print(dp[N-1])
