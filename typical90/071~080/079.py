H,W =map(int,input().split())
A = []
B = []
for i in range(W):
  a = list(map(int,input().split()))
  A.append(a)
for i in range(W):
  b = list(map(int,input().split()))
  B.append(b)
ans = 0
#左上から順にAをBにあわせていく
for i in range(H-1):
  for j in range(W-1):
    delta = B[i][j] - A[i][j]
    for ni,nj in [(i,j),(i,j+1),(i+1,j),(i+1,j+1)]:
      A[ni][nj] += delta
    ans += abs(delta)
can_match = True
#合わせられていないH+W-1個の要素が合致しているかを判定
for i in range(H):
  if A[i][W-1] != B[i][W-1]:
    can_match = False
for j in range(W):
  if A[H-1][j] != B[H-1][j]:
    can_match = False
if can_match:
  print('Yes')
  print(ans)
  exit()
else:
  print("No")