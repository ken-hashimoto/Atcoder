N = int(input())
A = list(map(int,input().split()))
A.sort()
Q = int(input())
def binary_search(M):
  left = -1
  right = N-1
  while left + 1 != right:
    mid = (left + right)//2
    if A[mid] < M:
      left = mid
    else:
      right = mid
  return right
for _ in range(Q):
  B = int(input())
  i = binary_search(B)
  if i-1 >= 0:
    print(min(abs(A[i] - B),abs(A[i-1] - B)))
  else:
    print(abs(A[i] - B))