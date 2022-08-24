N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
li = []
tmp = []
cnt_X = 0
cnt_Y = 0
ans = 0
for i in range(N):
  if A[i] > X or A[i] < Y:
    if len(tmp) > 0:
      if cnt_X > 0 and cnt_Y > 0:
        li.append(tmp)
      tmp = []
      cnt_X = 0
      cnt_Y = 0
    continue
  tmp.append(A[i])
  if A[i] == X:
    cnt_X += 1
  if A[i] == Y:
    cnt_Y += 1
  if i == N-1:
    if len(tmp) > 0:
      if cnt_X > 0 and cnt_Y > 0:
  	    li.append(tmp)
for item in li:
  M = len(item)
  r = 0
  cnt_X = 0
  cnt_Y = 0
  for l in range(M):
    while l > r:
      r += 1
    while (cnt_X == 0 or cnt_Y == 0) and r < M:
      if item[r] == X:
        cnt_X += 1
      if item[r] == Y:
        cnt_Y += 1
      r += 1
    if cnt_X > 0 and cnt_Y > 0:
      ans += M - r + 1
    if item[l] == X:
      cnt_X -= 1
    if item[l] == Y:
      cnt_Y -= 1
print(ans)