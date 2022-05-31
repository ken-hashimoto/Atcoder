H,W = map(int,input().split())
Grid = []
MOD = 10**9 + 7
for i in range(H):
  S = input()
  Grid.append(S)

#dp[i][j] = (S[i][j]にたどりつく経路数)
dp = [[0]*W for _ in range(H)]
#上端、左端のマスは壁にぶち当たるまで経路数1
for j in range(W):
  if Grid[0][j] == '#':
    break
  dp[0][j] = 1
for i in range(H):
  if Grid[i][0] == '#':
    break
  dp[i][0] = 1


#上から移動してくる場合と左から移動してくる場合に分けて考える
for i in range(1,H):
  for j in range(1,W):
    if Grid[i][j] == '#':
      continue
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp[i][j] %= MOD

#出力
print(dp[H-1][W-1])