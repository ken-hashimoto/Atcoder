def list_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            elif i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes


pl = list_primes(3 * 10**6)
T = int(input())
for _ in range(T):
    N = int(input())
    for p in pl:
        if N % p == 0:
            if N % p**2 == 0:
                print(p, N // p**2)
                break
            else:
                print(int((N // p) ** 0.5), p)
                break
