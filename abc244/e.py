from sys import stdin
input=lambda:stdin.readline().strip()
N,M,K,S,T,X = map(int,input().split())
X -= 1
S -= 1
T -= 1
G = [[] for _ in range(N)]
for i in range(M):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  G[u].append(v)
  G[v].append(u)
mod = 998244353
#dp[i][t][s] = (整数Xがs mod 2 回登場し、終点が頂点tであるような長さi+1の数列の個数)
dp = [[[0]*2 for _ in range(N+2)] for _ in range(K+2) ]
#求めるのはdp[K][T][0]
dp[0][S][0] = 1
for i in range(K+1):
  for t in range(N):
    for s in range(2):
      for nv in G[t]:
        if nv == X:
          dp[i+1][nv][(s+1)%2] = (dp[i+1][nv][(s+1)%2] + dp[i][t][s])%mod
        else:
          dp[i+1][nv][s] = (dp[i+1][nv][s] + dp[i][t][s])%mod
print(dp[K][T][0])