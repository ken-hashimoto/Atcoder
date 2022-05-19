H,W = map(int,input().split())
A = []
row = [0 for _ in range(H)] #row[i] = (i行目の総和)
column = [0 for _ in range(W)] #column[i] = (i列目の総和)
for i in range(H):
  a = list(map(int,input().split()))
  row[i] = sum(a)
  A.append(a)
for i in range(W):
  s = 0
  for j in range(H):
    s += A[j][i]
  column[i] = s
for i in range(H):
  ans_row = []
  for j in range(W):
    tmp = row[i] + column[j] - A[i][j]
    ans_row.append(tmp)
  print(*ans_row)