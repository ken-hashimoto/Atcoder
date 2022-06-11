X,A,D,N = map(int,input().split())
left = 1
right = N
def S(k):
  return A + (k-1)*D
if D == 0:
  print(abs(A-X))
  exit()
if D > 0:
  while left + 1 != right:
    mid = (left+right)//2
    if S(mid) >= X:
      right = mid
    else:
      left = mid
  ans = min(abs(S(left-1) - X),abs(S(left) - X), abs(S(left+1) - X))
  print(ans)
else:
  while left + 1 != right:
    mid = (left+right)//2
    if S(mid) >= X:
      left = mid
    else:
      right = mid
  ans = min(abs(S(left+1) - X),abs(S(left) - X), abs(S(left-1) - X))
  print(ans)
