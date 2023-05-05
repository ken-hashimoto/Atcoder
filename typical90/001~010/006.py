# res[i][c] := i 文字目以降で最初に文字 c が登場する index


def calc_next(S):
    N = len(S)
    res = [[N] * 26 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(26):
            res[i][j] = res[i + 1][j]
        res[i][ord(S[i]) - ord("a")] = i
    return res


N, K = map(int, input().split())
S = input()
ans = ""
nex = calc_next(S)

j = -1  # 今見てるところ
for i in range(K):
    for ordc in range(26):
        k = nex[j + 1][ordc]
        if N - k >= K - i:
            ans += chr(ord("a") + ordc)
            j = k
            break
print(ans)
