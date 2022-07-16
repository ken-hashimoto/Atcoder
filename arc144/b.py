import math
N,a,b = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
def check(m):
  plus = 0
  minus = 0
  for i in range(N):
    if A[i] == m:
      continue
    if A[i] < m:
      plus += math.ceil((m-A[i])/a)
    if A[i] > m:
      minus += (A[i]-m)//b 
  if plus <= minus:
    return True
  else:
    return False
ok = 0
ng = 10**9 +10
while ok + 1 != ng:
  mid = (ok+ng)//2
  if check(mid):
    ok = mid
  else:
    ng = mid
print(ok)