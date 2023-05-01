from collections import deque

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    C = list(map(int, input().split()))
    cost = [[-1 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    if C[0] == C[N - 1]:
        print(-1)
        continue
    cost[0][N - 1] = 0
    d = deque()
    d.append((0, N - 1))
    while d:
        takahashi, aoki = d.popleft()
        for nt in G[takahashi]:
            for na in G[aoki]:
                if cost[nt][na] >= 0:
                    continue
                if C[nt] == C[na]:
                    continue
                cost[nt][na] = cost[takahashi][aoki] + 1
                d.append((nt, na))
    print(cost[N - 1][0])
