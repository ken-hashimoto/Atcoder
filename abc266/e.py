N = int(input())
s = 1/6
dp = [0]*110
for i in range(1,N+1):
  for j in range(1,7):
    dp[i] += max(dp[i-1],j) * 1/6
print(dp[N])
