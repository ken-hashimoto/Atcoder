H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
ans = 0
for i in range(1,H-1):
  for j in range(1,W-1):
    #S[i][j]が角かどうかを判定
    #|  ..   .#   #.   ..
    #|  .#   ..   ..   #.
    if S[i][j] == "#":
      if S[i-1][j]==S[i-1][j-1]==S[i][j-1]==".":
        ans += 1
      if S[i+1][j]==S[i+1][j-1]==S[i][j-1]==".":
        ans += 1
      if S[i+1][j]==S[i+1][j+1]==S[i][j+1]==".":
        ans += 1
      if S[i-1][j]==S[i-1][j+1]==S[i][j+1]==".":
        ans += 1
    if S[i][j] == ".":
      if S[i-1][j]==S[i-1][j-1]==S[i][j-1]=="#":
        ans += 1
      if S[i+1][j]==S[i+1][j-1]==S[i][j-1]=="#":
        ans += 1
      if S[i+1][j]==S[i+1][j+1]==S[i][j+1]=="#":
        ans += 1
      if S[i-1][j]==S[i-1][j+1]==S[i][j+1]=="#":
        ans += 1
    #|  ##   #.   .#   ##
    #|  #.   ##   ##   .#
print(ans)

