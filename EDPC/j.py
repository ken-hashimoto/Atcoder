N = int(input())
cnt = {1:0, 2:0, 3:0}
A = list(map(int,input().split()))
for a in A:
  cnt[a] += 1
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
#dp[i][j][k] = (1貫,2貫,3貫乗った皿がそれぞれi,j,k枚あったときの全ての寿司がなくなるまでにかかる操作回数の期待値)
for i in range(N+1):
  for j in range(N+1):
    for k in range(N+1):
      nonzero = i + j + k
      if nonzero == 0:
        continue
      dp[i][j][k] = N / nonzero
      if i - 1 >= 0:
        dp[i][j][k] += dp[i-1][j][k] * (i / nonzero)
      if j - 1 >= 0:
        dp[i][j][k] += dp[i+1][j-1][k] * (j / nonzero)
      if k - 1 >= 0:
        dp[i][j][k] += dp[i][j+1][k-1] * (k / nonzero)
print(dp[cnt[1]][cnt[2]][cnt[3]])