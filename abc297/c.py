H, W = map(int, input().split())

ans = []
for i in range(H):
    S = input()
    tmp = []
    for i in range(W):
        if i > 0 and tmp[-1] == "P":
            tmp.append("C")
            continue
        if i < W - 1 and S[i] == "T" and S[i + 1] == "T":
            tmp.append("P")
        else:
            tmp.append(S[i])
    ans.append("".join(tmp))
for i in range(H):
    print(ans[i])
