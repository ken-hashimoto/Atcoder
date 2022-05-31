import sys

sys.setrecursionlimit(10**7)
N,M = map(int,input().split())
#dp(x)=(xを始点とする最長経路)
#もとめるのはmax{ dp(x)| 1<= x <= n }
#メモ化再帰を使う
G = [[] for _ in range(N+1)]
for _ in range(M):
  x,y = map(int,input().split())
  G[x].append(y)

seen = [False for _ in range(N+1)]
memo = [0 for _ in range(N+1)]

def dp(x):
  if seen[x]:
    return memo[x]
  longest = 0
  for to in G[x]:
    longest = max(longest,dp(to)+1)
  memo[x] = longest
  seen[x] = True
  return longest
ans = 0
for x in range(1,N+1):
  ans = max(ans,dp(x))
print(ans)