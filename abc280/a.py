H, W = map(int, input().split())
ans = 0
for _ in range(H):
    S = input()
    for s in S:
        if s == "#":
            ans += 1
print(ans)
