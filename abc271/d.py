N, S = map(int, input().split())
dp = [[] for _ in range(10**4 + 10)]
for i in range(N):
    a, b = map(int, input().split())
    if i == 0:
        dp[a] = ["H"]
        dp[b] = ["T"]
        continue
    dp_new = [[] for _ in range(10**4 + 10)]
    for j in range(10**4 + 10):
        if len(dp[j]) == i:
            if j + a <= S:
                dp_new[j + a] = dp[j] + ["H"]
            if j + b <= S:
                dp_new[j + b] = dp[j] + ["T"]
    dp = dp_new
if len(dp[S]) == N:
    print("Yes")
    print("".join(dp[S]))
else:
    print("No")
