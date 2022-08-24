def normalize(x1,y1,x2,y2):
  dx,dy = x1-x2,y1-y2
  if dx == 0: #y軸に平行であるとき
    if dy < 0:
      dy = -dy
    return (x1,"nil","nil","nil")
  if dx < 0:
    dx = -dx
    dy = -dy
  g = math.gcd(dx,dy)
  if g!= 0:
    dx = dx//g
    dy = dy//g
  sx,sy = dx,y1*dx-dy*x1
  g = math.gcd(sx,sy)
  if g != 0:
    sx = sx//g
    sy = sy//g
  return (dx,dy,sx,sy)

import math
N,K = map(int,input().split())
zahyou = []
for i in range(N):
  x,y = map(int,input().split())
  zahyou.append((x,y))
if K == 1:
  print("Infinity")
  exit()
ans = 0
d = dict()
for i in range(N):
  for j in range(i+1,N):
    x1,y1 = zahyou[i]
    x2,y2 = zahyou[j]
    normal = normalize(x1,y1,x2,y2)
    if not normal in d.keys():
      d[normal] = 1
    else:
      d[normal] += 1
for key in d.keys():
  if d[key] >= K*(K-1)//2:
    ans += 1
print(ans)