from itertools import accumulate


N,M = map(int,input().split())
A = list(map(int,input().split()))
S = [0] + list(accumulate(A))
#S[0] = 0
#S[i] = A[0] + ... + A[i-1]
res = 0
for i in range(M):
  res += (i+1) * A[i]
ans = res
for i in range(N):
  if i + M >= N:
    break
  res -= (S[i+M] - S[i])
  res += M * A[i+M]
  ans = max(res,ans)
print(ans)