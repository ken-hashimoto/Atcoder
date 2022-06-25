N,K,Q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))

now = [False]*(N+1)
for i in range(K):
  now[A[i]] = True
for i in range(Q):
  koma = A[L[i]-1]
  if koma < N and now[koma+1] == False:
    now[koma] = False
    A[L[i]-1] += 1
    now[koma+1] = True
print(*A)
