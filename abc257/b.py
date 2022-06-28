N,K,Q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))

A.append(N+1)
for i in range(Q):
  l = L[i]
  l -= 1
  if A[l+1] != A[l] + 1:
    A[l] = A[l] + 1
print(*A[:-1])
