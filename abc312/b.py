def check(S):
    R = [
        "###.?????",
        "###.?????",
        "###.?????",
        "....?????",
        "?????????",
        "?????....",
        "?????.###",
        "?????.###",
        "?????.###",
    ]
    for i in range(9):
        for j in range(9):
            if R[i][j] == "?":
                continue
            if R[i][j] != S[i][j]:
                return False
    return True


N, M = map(int, input().split())
S = []
ans = []
for i in range(N):
    s = list(input())
    S.append(s)
for i in range(N):
    for j in range(M):
        if not (i + 8 < N and j + 8 < M):
            continue
        SToCheck = []
        for k in range(i, i + 9):
            SToCheck.append((S[k][j : j + 9]))
        if check(SToCheck):
            ans.append((i + 1, j + 1))
for a in ans:
    i, j = a
    print(i, j)
