N = int(input())
time = 0
doukasen = []
ans = 0
for _ in range(N):
  A,B = map(int,input().split())
  time += A/B
  doukasen.append((A,B))
time = time/2
for i in range(N):
  a,b = doukasen[i]
  if time > a/b:
    ans += a
    time -= a/b
    continue
  ans += b*time
  print(ans)
  exit()