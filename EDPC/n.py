import itertools
import operator
#区間dp
N = int(input())
A = list(map(int,input().split()))
s = [0] + list(itertools.accumulate(A))
#s[i] = A[0] + ... + A[i-1]
#dp[l][r] = (区間[l,r)までのスライム、すなわちA[l:r]をひとつにするための最小コスト)
#求めたいのはdp[0][N]
INF = float('inf')
dp = [[INF]*(N+1) for _ in range(N+1)]
for w in range(1,N+1):
  for l in range((N+1)-w):
    r = l + w
    if w == 1:
      dp[l][r] = 0
    else:
      for m in range(l+1,r):
        #A[l] + ... + A[r-1] = s[r] - s[l]
        dp[l][r] = min(dp[l][r],dp[l][m] + dp[m][r] + (s[r] - s[l]))
print(dp[0][N])