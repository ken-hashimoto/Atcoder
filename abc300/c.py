def center_check(C, i, j):
    global H, W
    if C[i][j] == "#":
        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            return False
        if (
            C[i - 1][j - 1]
            == C[i - 1][j + 1]
            == C[i + 1][j - 1]
            == C[i + 1][j + 1]
            == "#"
        ):
            if C[i - 1][j] == C[i + 1][j] == C[i][j + 1] == C[i][j - 1] == ".":
                return True
    return False


H, W = map(int, input().split())
C = []
for i in range(H):
    c = list(input())
    C.append(c)
center = []
N = min(H, W)
ans = [0 for _ in range(N)]
for i in range(H):
    for j in range(W):
        if center_check(C, i, j):
            center.append((i, j))
for ct in center:
    i, j = ct
    size = 0
    while True:
        i -= 1
        j -= 1
        if i < 0 or i >= H or j < 0 or j >= W:
            break
        if C[i][j] == ".":
            break
        size += 1
    ans[size - 1] += 1
print(*ans)
