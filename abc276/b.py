N,M = map(int,input().split())
path = [[] for _ in range(N)]
for i in range(M):
  a,b = map(int,input().split())
  path[a-1].append(b)
  path[b-1].append(a)
for i in range(N):
  d = len(path[i])
  ans_li = [d] + sorted(path[i])
  print(*ans_li)
  