def f(a,b):
  return a**3 + a**2*b + a*b**2 + b**3
N = int(input())
ans = 10**20
for a in range(10**6+1):
  left = 0 #f(a,left) < N
  right = 10**6+1 #f(a,right) >= N
  if f(a,left) >= N:
    ans = min(ans,f(a,left))
    continue
  while left + 1 != right:
    mid = (left + right)//2
    cand = f(a,mid)
    if cand < N:
      left = mid
    else:
      right = mid
  ans = min(ans,f(a,right))
print(ans)