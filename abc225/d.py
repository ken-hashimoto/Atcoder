N,Q = map(int,input().split())
par = {i:-1 for i in range(1,N+1)}
child = {i:-1 for i in range(1,N+1)}
for _ in range(Q):
  q = list(map(int,input().split()))
  num = q[0]
  if num == 1:
    x,y = q[1],q[2]
    par[y] = x
    child[x] = y
  if num == 2:
    x,y = q[1],q[2]
    par[y] = -1
    child[x] = -1
  if num == 3:
    x = q[1]
    while par[x] != -1:
      x = par[x]
    ans = [x]
    while True:
      x = child[x]
      if x == -1:
        break
      ans.append(x)
    print(len(ans),*ans)