import math
import bisect


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2 * i, n + 1, i):
                prime[j] = False

    return prime


N = int(input())
era = sieve_of_eratosthenes(1000000)
primes = []
for i in range(len(era)):
    if era[i]:
        primes.append(i)
ans = 0
P = len(primes)
for i in range(P):
    a = primes[i]
    for j in range(i, P):
        b = primes[j]
        if a == b:
            continue
        if b > 10**4:
            break
        ind_left = bisect.bisect(primes, b)
        D = (N / (a**2 * b)) ** 0.5
        ind_right = bisect.bisect(primes, D)
        if ind_left >= ind_right:
            continue
        ans += ind_right - ind_left
        ## (N/(a**2 * b))**0.5以下の素数でa<b<cを満たすモノはいくつあるか？

print(ans)
