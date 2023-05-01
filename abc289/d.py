N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())
dp = [False for _ in range(X + 1)]
dp[0] = True
for i in range(X + 1):
    if dp[i]:
        for a in A:
            if i + a not in B and i + a <= X:
                dp[i + a] = True

if dp[X]:
    print("Yes")
else:
    print("No")
