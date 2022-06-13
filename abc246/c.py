N,K,X = map(int,input().split())
A = list(map(int,input().split()))
used_coupon = 0
for i in range(N):
  if used_coupon >= K:
    break
  used_coupon += A[i]//X
  A[i] = A[i]%X
if used_coupon > K:
  too_use = used_coupon - K
  ans = sum(A) + too_use * X
if used_coupon < K:
  A.sort(reverse=True)
  not_use = K - used_coupon
  if 1 <= not_use < N:
    ans = sum(A[not_use:])
  else:
    ans = 0

print(ans)
