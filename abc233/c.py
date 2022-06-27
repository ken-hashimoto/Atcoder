import sys
sys.setrecursionlimit(10**7)
N,X = map(int,input().split())
A = [list(map(int, input().split()))[1:] for _ in range(N)]
ans = 0

def dfs(i,now):
  global ans
  if i == N:
    if now == X:
      ans += 1
    return
  for a in A[i]:
    dfs(i+1,now*a)
  return

dfs(0,1)
print(ans)