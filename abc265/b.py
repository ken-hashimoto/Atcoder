N,M,T = map(int,input().split())
A = [0] + list(map(int,input().split()))
time = T
now = 1
d = {i:0 for i in range(N+1)}
for i in range(M):
  x,y = map(int,input().split())
  d[x] = y
for i in range(1,N):
  time -= A[i]
  print(time)
  if time <= 0:
    print("No")
    exit()
  if d[i+1] > 0:
    time += d[i+1]
  print(time)

print("Yes")