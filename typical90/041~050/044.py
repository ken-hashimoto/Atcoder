N,Q = map(int,input().split())
A = list(map(int,input().split()))
minus_ind = 0
for _ in range(Q):
  T,x,y = map(int,input().split())
  x,y = x-1,y-1
  if T == 1:
    A[(x-minus_ind)%N],A[(y-minus_ind)%N] = A[(y-minus_ind)%N],A[(x-minus_ind)%N]
  if T == 2:
    minus_ind += 1
  if T == 3:
    x_ind = (x-minus_ind)%N
    print(A[x_ind])