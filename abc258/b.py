N = int(input())
A = [list(input()) for _ in range(N)]

d = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

ans = 0
for i in range(N):
  for j in range(N):
    #A[i][j]がスタート地点
    for v in d:
      tmp = A[i][j]
      x = i
      y = j
      for k in range(N-1):
        x += v[0]
        y += v[1]
        tmp += A[x%N][y%N]
      tmp = int(tmp)
      ans = max(ans,tmp)
print(ans)