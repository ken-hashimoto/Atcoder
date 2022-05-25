N,K = map(int,input().split())
MOD = 10**9 + 7
ans = 1
for i in range(N):
  if i == 0:
    ans = K
  elif i == 1:
    ans *= K-1
    ans %= MOD
  else:
    ans *= pow(K-2,N-2,MOD)
    ans %= MOD
print(ans%MOD)
