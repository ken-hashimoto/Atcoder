Q = int(input())
up = []
down = []
for i in range(Q):
  t,x = map(int,input().split())
  if t == 1:
    up.append(x)
  if t == 2:
    down.append(x)
  if t == 3:
    x -= 1
    if 0 <= x < len(up):
      print(up[-x-1])
    else:
      print(down[x-len(up)])