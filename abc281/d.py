N,K,D = map(int,input().split())
#dp[i][j] = (相異なるi個の和でDで割ったあまりがjとなるようなものの最大値)
dp = [[-1 for _ in range(D)] for _ in range(K+1)]
A = list(map(int,input().split()))
dp[0][0] = 0
for i,a in enumerate(A):
  if i == 0:
    dp[1][a%D] = a
    continue
  for j in range(K-1,-1,-1):
    for k in range(D):
      if dp[j][k] == -1:
        continue
      dp[j+1][(k+a)%D] = max(dp[j][k] + a,dp[j+1][(k+a)%D])
print(dp[K][0])
