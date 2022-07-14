import math


N = int(input())
points = []
for _ in range(N):
  x,y = map(int,input().split())
  points.append((x,y))
ans = []
for i in range(N):
  for j in range(N):
    xi,yi = points[i]
    xj,yj = points[j]
    dx = xi-xj
    dy = yi-yj
    g = math.gcd(dx,dy)
    tmp = (dx,dy)
    if g != 0:
      tmp = (dx//g,dy//g) 
    if tmp != (0,0):
      ans.append(tmp)
print(len(set(ans)))
