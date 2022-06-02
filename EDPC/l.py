N = int(input())
A = list(map(int,input().split()))
#dp[l][r] = (A[l:r]のときの答え、左半開区間となってることに注意)
dp = [[0]*(N+1) for _ in range(N+1)]
for w in range(1,N+1):
  for l in range(N-w+1):
    r = l + w
    if (l-r)%2 == N%2:
      #太郎の番
      dp[l][r] = max(dp[l][r-1]+A[r-1],dp[l+1][r]+A[l])
    else:
      #次郎の番
      dp[l][r] = min(dp[l][r-1]-A[r-1],dp[l+1][r]-A[l])
print(dp[0][N])