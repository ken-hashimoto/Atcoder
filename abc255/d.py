import bisect
import itertools
import operator
N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
cum = [0] + list(itertools.accumulate(A))
print(cum)
#cum[i] = A[0] + ... + A[i-1]
for i in range(Q):
  X = int(input())
  X_ind_left = bisect.bisect_left(A,X)
  X_ind_right = bisect.bisect_right(A,X)
  print(X_ind_left,X_ind_right)
  ans = (X*(X_ind_left) - cum[X_ind_left]) + (cum[N] - cum[X_ind_right]) - X*(N-X_ind_right)
  print(ans)