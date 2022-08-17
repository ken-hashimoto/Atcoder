N = int(input())
A = list(map(int,input().split()))
mod = 998244353 
dp = [0]*(N+1)
dp[0] = 1
ans = 0
#dp[i] = (マスiをちょうど踏む確率)
#求めるのはdp[i] * (A[i]+1)/A[i]の0からN-1までの総和
#ここでdp[i] * (A[i]+1)/A[i]はマスiでサイコロを振る回数の期待値


#配るdp
#dp[i] * 1/A[i]をdp[i+1] , ... dp[i+A[i]]まで配る

#dp[0] = 1 (マス1には最初からいるので)
#dp[1] = dp[0] * 1/A[0] <- 1/(A[0]+1)ではないことに注意!

#いちいち配ると計算量が多いのでimos法で配る
for i in range(0,N-1):
  if i-1 > 0:
    dp[i] += dp[i-1]
  dp[i] %= mod
  val = dp[i] * pow(A[i],mod-2,mod) %mod
  dp[i+1] += val
  dp[i+A[i]+1] -= val
  ans += dp[i] * (A[i]+1) * pow(A[i],mod-2,mod) % mod 
  ans %= mod
  
print(ans%mod)