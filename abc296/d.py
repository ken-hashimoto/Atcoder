import math

INF = float("inf")
N, M = map(int, input().split())
ans = INF

for a in range(1, min(math.floor(M**0.5) + 10, N + 1)):
    b = math.ceil(M / a)
    X = a * b
    if 1 <= b <= N and 1 <= a <= N and X >= M:
        ans = min(ans, a * b)
if ans == INF:
    print(-1)
else:
    print(ans)
