from collections import deque

N = int(input())
G = dict()
seen = dict()
for i in range(N):
    A, B = map(int, input().split())
    if A not in G.keys():
        G[A] = [B]
    else:
        G[A].append(B)
    if B not in G.keys():
        G[B] = [A]
    else:
        G[B].append(A)
    seen[A] = False
    seen[B] = False

ans = 0
d = deque(1)
while d:
    v = d.pop()
    for nv in G[v]:
        if seen[nv]:
            continue
        seen[nv] = True
        ans = max(ans, nv)
        d.append(nv)
print(ans)
