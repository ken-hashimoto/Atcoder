import itertools


N,K = map(int,input().split())
A = list(map(int,input().split()))
l = 0
r = 0
c = [0] + list(itertools.accumulate(A))
#c[0] = 0
#c[1] = A[0]
#...
#c[i] = A[0] + ... + A[i-1]
ans = 0
d = dict()
#c[r+1] - c[l] = K
for r in range(N+1):
  if c[r] - K in d.keys():
    ans += d[c[r]-K]
  if c[r] in d.keys():
    d[c[r]] += 1
  else:
    d[c[r]] = 1
print(ans)