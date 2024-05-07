H, W = map(int, input().split())
C = []
ans = []
for i in range(H):
    c = input()
    C.append(list(c))
for j in range(W):
    cnt = 0
    for i in range(H):
        if C[i][j] == "#":
            cnt += 1
    ans.append(cnt)
print(*ans)
