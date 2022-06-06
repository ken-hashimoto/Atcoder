import sys
sys.setrecursionlimit(10**7)

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
  x,y = list(map(int,input().split()))
  G[x].append(y)
  G[y].append(x)
MOD = 10**9 + 7

#頂点1を根としてグラフを木とみる
#dp[i][j] = (頂点iが色jであるとき、頂点iを根としたときの部分木の塗り方の数)
#0が白、1が黒
dp = [[1,1] for _ in range(N+1)]
def dfs(parent_v,v): #帰りがけ順でdpテーブルを埋める
  for nv in G[v]:
    if nv == parent_v: #逆行を防ぐ
      continue
    dfs(v,nv)
    dp[v][0] *= dp[nv][0] + dp[nv][1]
    dp[v][1] *= dp[nv][0]
    dp[v][0] %= MOD
    dp[v][1] %= MOD


dfs(0,1)
print((dp[1][0] + dp[1][1])%MOD)