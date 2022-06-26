from bisect import bisect_left


N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
for _ in range(Q):
  x = int(input())
  print(bisect_left(A,x))