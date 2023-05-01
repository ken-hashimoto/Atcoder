import sys
sys.setrecursionlimit(10**7)
N,Q = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
  a,b = map(int,input().split())
  G[a].append(b)
  G[b].append(a)
d_cnt = dict()
for i in range(N+1):
  d_cnt[i] = 0
for i in range(Q):
  p,x = map(int,input().split())
  d_cnt[p] += x
ans = [0 for _ in range(N+1)]
def dfs(v,parent_v):
  ans[v] += d_cnt[v]
  for nv in G[v]:
    if nv == parent_v:
      continue
    ans[nv] = ans[v]
    dfs(nv,v)

dfs(1,0)
print(*ans[1:])