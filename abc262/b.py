N,M = map(int,input().split())
graph = [[False]*N for _ in range(N)]
ans = 0
for i in range(M):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  graph[u][v] = True
  graph[v][u] = True
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if graph[i][j] and graph[j][k] and graph[k][i]:
        ans += 1
print(ans)