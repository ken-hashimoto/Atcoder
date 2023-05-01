N, M = map(int, input().split())
A = set(map(int, input().split()))
ans = []
tmp = []

for i in range(1, N + 1):
    if i in A:
        tmp.append(i)
        continue
    ans.append(i)
    ans += tmp[::-1]
    tmp = []
print(*ans)
