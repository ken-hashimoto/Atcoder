H,W = map(int,input().split())
G = []
for i in range(H):
  G.append(list(input()))
seen = [[False]*W for _ in range(H)]
i = 0
j = 0
while True:
  seen[i][j] = True
  if G[i][j] == "U":
    if i == 0:
      print(i+1,j+1)
      exit()
    i -= 1
  elif G[i][j] == "D":
    if i == H-1:
      print(i+1,j+1)
      exit()
    i += 1
  elif G[i][j] == "L":
    if j == 0:
      print(i+1,j+1)
      exit()
    j -= 1
  elif G[i][j] == "R":
    if j == W-1:
      print(i+1,j+1)
      exit()
    j += 1
  if seen[i][j]:
    print(-1)
    exit()
