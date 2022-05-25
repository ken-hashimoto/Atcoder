def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
N = int(input())
#Nの素因数の数をSとするとceil(log_{2}S)となりそう
S = len(prime_factorize(N))
import math
print(math.ceil(math.log2(S)))

