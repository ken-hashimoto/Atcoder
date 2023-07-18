# 強連結成分分解(SCC)をする
# 分解したそれぞれの成分に対してnC2をとればよい

import sys

sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]  # 逆向きの辺を格納
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    RG[b - 1].append(a - 1)
seen = [False for _ in range(N)]
PairOfNV = []  # (num,v)
cnt = 0


def dfs(v, G, seen):
    # dfsしながら帰りがけの順で番号を頂点に付与
    seen[nv] = True
    global cnt
    for nv in G[v]:
        if seen[nv]:
            continue
        dfs(nv, G, seen)
    PairOfNV.append((cnt, v))
    cnt += 1


for v in range(N):
    if seen[v]:
        continue
    dfs(v, G, seen)


def dfs2(v, G, seen):
    global tmp
    tmp.append(v)
    for nv in G[v]:
        if seen[nv]:
            continue
        seen[nv] = True
        dfs2(nv, G, seen)


PairOfNV.sort(key=lambda x: -x[0])
seen = [False for _ in range(N)]

ans = 0
for _, v in PairOfNV:
    if seen[v]:
        continue
    tmp = []
    # 逆向きの辺を使ってDFSする
    dfs2(v, RG, seen)
    V_cnt = len(tmp)

    ans += V_cnt * (V_cnt - 1) // 2
print(ans)
