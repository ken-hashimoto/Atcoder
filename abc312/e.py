N = int(input())
G = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
for i in range(N):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    if z2 < z1:
        z1, z2 = z2, z1
    if y2 < y1:
        y1, y2 = y2, y1
    if x2 < x1:
        x1, x2 = x2, x1
    for z in range(z1, z2):
        for y in range(y1, y2):
            for x in range(x1, x2):
                G[x][y][z] = i
adj = [set() for _ in range(N)]

for x in range(0, 101):
    for y in range(0, 101):
        for z in range(0, 100):
            if G[x][y][z] != G[x][y][z + 1]:
                if G[x][y][z] == -1 or G[x][y][z + 1] == -1:
                    continue
                adj[G[x][y][z]].add(G[x][y][z + 1])
                adj[G[x][y][z + 1]].add(G[x][y][z])
for y in range(0, 101):
    for z in range(0, 101):
        for x in range(0, 100):
            if G[x][y][z] != G[x + 1][y][z]:
                if G[x][y][z] == -1 or G[x + 1][y][z] == -1:
                    continue
                adj[G[x][y][z]].add(G[x + 1][y][z])
                adj[G[x + 1][y][z]].add(G[x][y][z])
for z in range(0, 101):
    for x in range(0, 101):
        for y in range(0, 100):
            if G[x][y][z] != G[x][y + 1][z]:
                if G[x][y][z] == -1 or G[x][y + 1][z] == -1:
                    continue
                adj[G[x][y][z]].add(G[x][y + 1][z])
                adj[G[x][y + 1][z]].add(G[x][y][z])
for a in adj:
    print(len(a))
