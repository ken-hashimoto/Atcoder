import bisect
import itertools

N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
cum = list(itertools.accumulate(A))
def is_ok(m):
  global A
  ind = bisect.bisect_right(A,m)
  s = cum[ind-1] + m * (N-ind)
  if s >= K * m:
    return True
  else:
    return False
ok = 0
ng = 10**18
while ok + 1 != ng:
  mid = (ok + ng)//2
  if is_ok(mid):
    ok = mid
  else:
    ng = mid
print(ok)
