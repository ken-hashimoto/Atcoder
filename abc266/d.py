from copy import deepcopy


N = int(input())
#dp[i][X] = (i秒目まで適切に行動し座標Xにいるときのスコア)
#dp[T_N]を求めたい
INF = float('inf')
dp_old = [0,-INF,-INF,-INF,-INF]
dp_new = [0,-INF,-INF,-INF,-INF]
now = 0
for i in range(N):
  T,X,A = map(int,input().split())
  for j in range(5):
    time = T - now
    r = min(time,5)
    for k in range(-r,r+1):
      if j + k < 0 or j + k >= 5:
        continue
      if j + k == X:
        dp_new[j+k] = max(dp_new[j+k],dp_old[j]+A)
      else:
        dp_new[j+k] = max(dp_old[j],dp_new[j+k])
  dp_old = deepcopy(dp_new)
  now = T
print(dp_new)
print(max(dp_new))