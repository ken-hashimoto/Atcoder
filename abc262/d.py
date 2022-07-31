N = int(input())
A = list(map(int,input().split()))
MOD = 998244353
ans = 0
#dp[i][j][k] = i項の和でをjで割ったあまりがk(0 <= k <j)であるような選び方の総数
#求めるのはdp[i][i][0]のiをまわした時の和
dp = [[[0]*(100+1) for _ in range(100+1)] for __ in range(N+1)]
# for j in range(1,101):
#   dp[1][j][A[0] % j] += 1
for i in range(N):
  #A[i]を含めるか含めないか
  for j in range(1,N+1):
    for k in range(j):
      #含める場合
      dp[i+1][j][(k + A[i-1])%j] += max(dp[i][j][k]%MOD,1)
for i in range(1,N+1):
  ans += dp[i][i][0]%MOD
print(ans%MOD)
print(dp)