import itertools
N,Q = map(int,input().split())
banmen = [0]*(N+1)
for i in range(Q):
  l,r = map(int,input().split())
  l -= 1
  banmen[l] += 1
  banmen[r] -= 1
cumsum = list(itertools.accumulate(banmen))
ans = ["0" for _ in range(N)]
for i in range(N):
  if cumsum[i]%2 == 1:
    ans[i] = "1"
print(''.join(ans))