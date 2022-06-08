H,W = map(int,input().split())
memo = []
for i in range(H):
  S = input()
  for j in range(W):
    if S[j] == "o":
      memo.append((i,j))
sx,sy = memo[0][0],memo[0][1]
gx,gy = memo[1][0],memo[1][1]
print(abs(sx-gx) + abs(sy-gy))