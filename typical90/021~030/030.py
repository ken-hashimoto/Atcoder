N, K = map(int, input().split())
ans = 0
factors = [0 for _ in range(N + 1)]
for i in range(2, N + 1):
    if factors[i] != 0:
        continue
    # i は素数
    for j in range(i, N + 1, i):
        factors[j] += 1
for i in range(N + 1):
    if factors[i] >= K:
        ans += 1
print(ans)
