N,D = map(int,input().split())
is_destroyed = [False]*N
start = []
end = []
for i in range(N):
  #0-indexedで半開区間で考える
  l,r = map(int,input().split())
  l -= 1
  start.append((l,r,i))
  end.append((l,r,i))
start.sort()
ind = 0
end.sort(key=lambda x:x[1])
ans = 0
for l,r,i in end:
  if is_destroyed[i]:
    continue
  if ind == N:
    break
  is_destroyed[i] = True
  ans += 1
  #r-1,r,...,r+d-2を壊す
  #その際に一緒に壊れる壁を探す
  #一緒に壊れるのは「始点<r+d-2」をみたす壁
  while start[ind][0] <= r+D-2:
    is_destroyed[start[ind][2]] = True
    ind += 1
    if ind == N:
      break
print(ans)