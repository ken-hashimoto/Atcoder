from collections import defaultdict
N,K = map(int,input().split())
A = list(map(int,input().split()))
#尺取り法を用いる
ans = 0
d = defaultdict(int)
left = 0
for right in range(N):
  d[A[right]] += 1
  while left < min(right,N) and len(d) > K:
    d[A[left]] -= 1
    if d[A[left]] == 0:
      del d[A[left]]
    left += 1
  ans = max(ans,right - left + 1)
print(ans)
