N = int(input())
P = list(map(int,input().split()))
d = dict()
for i in range(N):
  d[P[i]] = i+1
Q = []
for i in range(1,N+1):
  Q.append(d[i])
print(*Q)