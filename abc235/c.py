N,Q = map(int,input().split())
A = list(map(int,input().split()))
d = dict()
for i,a in enumerate(A):
  if not a in d:
    d[a] = [i+1]
  else:
    d[a].append(i+1)
for _ in range(Q):
  x,k = map(int,input().split())
  if not x in d:
    print(-1)
    continue
  if len(d[x]) < k:
    print(-1)
    continue
  print(d[x][k-1])