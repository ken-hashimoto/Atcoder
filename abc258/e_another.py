N,Q,X = map(int,input().split())
W = list(map(int,input().split()))
#周期性を考える
#鳩ノ巣原理からN+1回箱詰めをした時点で周期が発生する
 
PotatoCnt = [0]*N 
#Potato[i] = (i個目から箱詰めを開始した場合に何個のじゃがいもを箱に詰めることになるか)
NextPotato = [0]*N
#NextPotato[i] = (i個目から箱詰めを開始してそれが完了した場合、次に入れることになるじゃがいもはどれか）
WW = W + W
 
S = sum(W)
if X > S:
  #Xが非常に大きい場合
  for i in range(N):
    PotatoCnt[i] += (X//S)*N
  X = X%S 
#しゃくとり法を用いる
r = 0
s = 0
for l in range(N):
  while s < X:
    s += WW[r]
    r += 1
  PotatoCnt[l] += r - l
  NextPotato[l] = r%N
  s -= WW[l]

#ダブリング
#制約でKは13桁なので2^44の14桁くらいをとっておく
dp = [[0]*N for _ in range(45)]
#dp[i][j] = じゃがいもjから2^i回箱詰めしたあとに到達するジャガイモ
# 初期条件
for j in range(N):
    dp[0][j] = NextPotato[j]

# 遷移
for i in range(1, 45):
    for j in range(N):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]


for _ in range(Q):
  K = int(input())
  K -= 1
  i = 0
  ans = 0
  while K :
    if K & 1:
      ans = dp[i][ans]
    K >>= 1
    i += 1
  print(PotatoCnt[ans])
  