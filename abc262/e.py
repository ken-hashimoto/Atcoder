mod = 998244353
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]


def init(n):
    for i in range(2, n + 1):
        fac.append(fac[-1] * i % mod)
        inv.append(-inv[mod % i] * (mod // i) % mod)
        finv.append(finv[-1] * inv[-1] % mod)


def com(n, k, mod):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod
N,M,K = map(int,input().split())
d = [0]*N
for i in range(M):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  d[u] += 1
  d[v] += 1
even = []
odd = []
ans = 0
init(N)
for i in range(N):
    if d[i] % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
even_cnt = len(even)
odd_cnt = len(odd)
for k in range(0,K+1,2):
    l = K - k
    #oddからk個選ぶ
    if k <= odd_cnt and l <= even_cnt:
        ans += com(odd_cnt,k,mod) * com(even_cnt,l,mod)
        ans %= mod
print(ans)
