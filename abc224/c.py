N = int(input())
points = []
ans = 0
for _ in range(N):
  X,Y = map(int,input().split())
  points.append((X,Y))
for i in range(N):
  x1,y1 = points[i]
  for j in range(i,N):
    x2,y2 = points[j]
    for k in range(j,N):
      x3,y3 = points[k]
      if (x1-x2)*(y2-y3) != (y1-y2)*(x2-x3):
        ans += 1
print(ans)