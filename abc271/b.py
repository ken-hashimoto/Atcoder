N,Q = map(int,input().split())
seq = []
for i in range(N):
  A = list(map(int,input().split()))[1:]
  seq.append(A)
for i in range(Q):
  s,t = map(int,input().split())
  print(seq[s-1][t-1])
