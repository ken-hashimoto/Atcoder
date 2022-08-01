import itertools
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mod = 998244353
#dp[i][c]...最後の項がcである長さiの数列で条件を満たすもの
dp = [[0]*(3010) for _ in range(N+1)]
for c in range(A[0],B[0]+1):
  dp[0][c] = 1
for i in range(1,N):
  cum = list(itertools.accumulate(dp[i-1]))
  for c in range(A[i],B[i]+1):
    dp[i][c] = cum[c]
    dp[i][c] %= mod
print(sum(dp[N-1])%mod)