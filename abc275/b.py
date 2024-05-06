a, b, c, d, e, f = map(int, input().split())
mod = 998244353

a = a % mod
b = b % mod
c = c % mod
d = d % mod
e = e % mod
f = f % mod
print(((a * b * c) % mod - (d * e * f) % mod) % mod)
