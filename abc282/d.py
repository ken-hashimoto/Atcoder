from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
colors = [-1 for i in range(N)]  # 1がblack,0がwhite
ans = N * (N - 1) // 2 - M
for v in range(N):
    # 頂点vが含まれる連結成分を探索する
    if colors[v] != -1:
        continue
    colors[v] = 0
    black_cnt = 0
    white_cnt = 1
    d = deque()
    d.append(v)
    while d:
        qv = d.popleft()
        for nv in G[qv]:
            if colors[nv] != -1:
                if colors[nv] == colors[qv]:
                    # 入力はすでに二部グラフではない
                    print(0)
                    exit()
                continue
            colors[nv] = 1 - colors[qv]
            if colors[nv] == 0:
                white_cnt += 1
            if colors[nv] == 1:
                black_cnt += 1
            d.append(nv)
    ans -= black_cnt * (black_cnt - 1) // 2
    ans -= white_cnt * (white_cnt - 1) // 2
print(ans)
