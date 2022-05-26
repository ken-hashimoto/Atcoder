H,W = map(int,input().split())
R,C = map(int,input().split())
blocks = []
ans = 0
for i in range(1,H+1):
  for j in range(1,W+1):
    blocks.append((i,j))
for i,j in [(R+1,C),(R-1,C),(R,C+1),(R,C-1)]:
  if (i,j) in blocks:
    ans += 1
print(ans)