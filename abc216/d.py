from collections import deque


N,M = map(int,input().split())
length = []
cnt = {i:0 for i in range(1,N+1)}
location = {i:[] for i in range(1,N+1)}
balls = []
d = deque()
for i in range(M):
  k = int(input())
  length.append(k)
  a = list(map(int,input().split()))
  balls.append(a)
  cnt[a[0]] += 1
  location[a[0]].append((i,0))
  #balls[i][0] = a[0]ということ
  if cnt[a[0]] == 2:
    d.append(a[0])
while d:
  v = d.popleft()
  for i,j in location[v]:
    if j+1 < length[i]:
      cnt[balls[i][j+1]] += 1
      location[balls[i][j+1]].append((i,j+1))
      if cnt[balls[i][j+1]] == 2:
        d.append(balls[i][j+1])
for i in range(1,N+1):
  if cnt[i] != 2:
    print("No")
    exit()
print("Yes")
