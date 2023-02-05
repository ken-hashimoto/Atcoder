X, K = map(int, input().split())
for i in range(K + 1):
    s = 10**i // 2
    X = (X + s) // 10**i * 10**i
print(X)
