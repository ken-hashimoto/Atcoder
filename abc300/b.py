def shift(s, t, A):
    global H, W
    res = []
    for i in range(H):
        res.append(A[(i + s) % H])
    new_res = [["." for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            new_res[i][j] = res[i][(j + t) % W]
    return new_res


def check(A, B):
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]:
                return False
    return True


H, W = map(int, input().split())
A = []
for i in range(H):
    a = list(input())
    A.append(a)
B = []
for j in range(H):
    b = list(input())
    B.append(b)
for s in range(H):
    for t in range(W):
        res = shift(s, t, A)
        if check(B, res):
            print("Yes")
            exit()
print("No")
