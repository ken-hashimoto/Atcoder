import itertools
N,M = map(int,input().split())
graph_t = [[False]*(N+1) for _ in range(N+1)]
graph_a = [[False]*(N+1) for _ in range(N+1)]
for i in range(M):
  a,b = map(int,input().split())
  graph_t[a][b] = True
  graph_t[b][a] = True
for i in range(M):
  a,b = map(int,input().split())
  graph_a[a][b] = True
  graph_a[b][a] = True

for p in itertools.permutations(range(1,N+1),N):
  p = [0] + list(p)
  Is_same = True
  for i in range(1,N+1):
    for j in range(1,N+1):
      if graph_t[i][j]:
        if not graph_a[p[i]][p[j]]:
          Is_same = False
  if Is_same:
    print("Yes")
    exit()

print("No")