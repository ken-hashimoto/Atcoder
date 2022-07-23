# sys.stdin.readline()
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
X = list(map(int,input().split()))
#dp[i][c] = (i回コイントスをし終わったときのカウンタの値がcであるときのもらえるお金の最大値)
bonus = {i:0 for i in range(N+1)}
for i in range(M):
  c,y = map(int,input().split())
  bonus[c] = y
dp = [[-1]*(N+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
  for c in range(N):
    if dp[i][c] >= 0:
    	dp[i+1][min(c+1,N)] = dp[i][c] + X[i]
    	dp[i+1][min(c+1,N)] += bonus[c+1]
    	dp[i+1][0] = max(dp[i][0],dp[i][c],dp[i+1][0])
print(max(dp[N]))