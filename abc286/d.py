N, X = map(int, input().split())
dp = [False for _ in range(X + 1)]
dp_new = [False for _ in range(X + 1)]
dp_new[0] = True
for i in range(N):
    A, B = map(int, input().split())
    dp = dp_new
    dp_new = [False for _ in range(X + 1)]
    for j in range(X + 1):
        if dp[j]:
            for k in range(B + 1):
                if j + A * k <= X:
                    dp_new[j + A * k] = True
print("Yes" if dp_new[X] else "No")
