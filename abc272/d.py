from collections import deque

N, M = map(int, input().split())
d = deque()
d.append((0, 0, 0))
ans = [[-1 for i in range(N)] for j in range(N)]
ans[0][0] = 0
dxy = []
for i in range(N):
    for j in range(N):
        if i**2 + j**2 == M:
            dxy.append((i, j))
while d:
    x, y, t = d.popleft()
    for dx, dy in dxy:
        if 0 <= x + dx < N and 0 <= y + dy < N:
            if ans[x + dx][y + dy] == -1:
                ans[x + dx][y + dy] = t + 1
                d.append((x + dx, y + dy, t + 1))
        if 0 <= x + dx < N and 0 <= y - dy < N:
            if ans[x + dx][y - dy] == -1:
                ans[x + dx][y - dy] = t + 1
                d.append((x + dx, y - dy, t + 1))
        if 0 <= x - dx < N and 0 <= y + dy < N:
            if ans[x - dx][y + dy] == -1:
                ans[x - dx][y + dy] = t + 1
                d.append((x - dx, y + dy, t + 1))
        if 0 <= x - dx < N and 0 <= y - dy < N:
            if ans[x - dx][y - dy] == -1:
                ans[x - dx][y - dy] = t + 1
                d.append((x - dx, y - dy, t + 1))
for a in ans:
    print(*a)
