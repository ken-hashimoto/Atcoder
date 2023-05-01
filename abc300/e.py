from functools import lru_cache

N = int(input())
mod = 998244353
inv5 = pow(5, -1, mod)


@lru_cache(maxsize=10**6)
def dp(a, b, c):
    if (a, b, c) == (0, 0, 0):
        return 1
    ans = 0
    if a >= 1:  # 2の目
        ans += dp(a - 1, b, c)
    if b >= 1:  # 3の目
        ans += dp(a, b - 1, c)
    if a >= 2:  # 4の目
        ans += dp(a - 2, b, c)
    if c >= 1:  # 5の目
        ans += dp(a, b, c - 1)
    if a >= 1 and b >= 1:  # 6の目
        ans += dp(a - 1, b - 1, c)
    return ans * inv5 % mod


a, b, c = 0, 0, 0
while N % 2 == 0:
    N //= 2
    a += 1
while N % 3 == 0:
    N //= 3
    b += 1
while N % 5 == 0:
    N //= 5
    c += 1
if N != 1:
    print(0)
else:
    print(dp(a, b, c))
