N = int(input())
G = [[-1]*N for _ in range(N)]
now = 0
num = 1
while now < N:
  G[0][now] = num
  num += 1
  now += 2
now = 1
while now < N:
  G[0][now] = num
  num += 1
  now += 2
for j in range(N):
  for i in range(1,N):
    G[i][j] = G[i-1][j] + N

for g in G:
  print(*g)