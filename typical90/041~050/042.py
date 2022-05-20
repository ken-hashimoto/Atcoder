K = int(input())
MOD = 10**9 + 7
if K%9 != 0:
  print(0)
  exit()

#Kは9の倍数
dp = [0 for _ in range(K+1)]
#dp[k] = (各桁の数字の和がkであるような自然数がいくつあるか)
#求めるのはdp[K]
for i in range(1,10):
  dp[i] = 1
for i in range(2,K+1):
  for j in range(1,10):
    if i-j > 0:
      dp[i] += dp[i-j]
      dp[i] %= MOD
print(dp[K])