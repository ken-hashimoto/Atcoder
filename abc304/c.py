import sys

sys.setrecursionlimit(3000)

N, D = map(int, input().split())
X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]
seen = [False for _ in range(N)]
for i in range(N):
    x, y = map(int, input().split())
    X[i] = x
    Y[i] = y


def is_connected(x1, y1, x2, y2):
    l = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return l <= D**2


def dfs(v):
    seen[v] = True
    for nv in range(N):
        if not seen[nv] and is_connected(X[v], Y[v], X[nv], Y[nv]):
            dfs(nv)


dfs(0)

for i in range(N):
    if seen[i]:
        print("Yes")
    else:
        print("No")
