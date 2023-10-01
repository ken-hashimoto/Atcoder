A = []
B = []
C = []
for i in range(4):
    a = list(input())
    A.append(a)
for i in range(4):
    b = list(input())
    B.append(b)
for i in range(4):
    c = list(input())
    C.append(c)


def kaiten(X):
    # 右に90度回転
    res = []
    for i in range(4):
        r = []
        for j in range(4):
            r.append(X[3 - j][i])
        res.append(r)
    return res


def isInner(i, j):
    return 4 <= i < 8 and 4 <= j < 8


def isValid(R):
    for p in range(4 + 4 + 4):
        for q in range(4 + 4 + 4):
            if not isInner(p, q) and R[p][q] == "#":
                return False
    return True


def cut(X):
    tmp = X[4:8]
    res = []
    for i in range(4):
        res.append(tmp[i][4:8])
    return res


def heikou(X):
    res = []
    for i in range(4 + 4):
        for j in range(4 + 4):
            sheet = [list("." * (4 + 4 + 4)) for _ in range(4 + 4 + 4)]
            for k in range(4):
                for l in range(4):
                    sheet[i + k][j + l] = X[k][l]
            if isValid(sheet):
                res.append(cut(sheet))
    return res


heikouA = heikou(A)
heikouB = heikou(B)
heikouC = heikou(C)

heikoukaitenA = []
heikoukaitenB = []
heikoukaitenC = []

for a in heikouA:
    for i in range(4):
        a = kaiten(a)
        heikoukaitenA.append(a)
for b in heikouB:
    for i in range(4):
        b = kaiten(b)
        heikoukaitenB.append(b)
for c in heikouC:
    for i in range(4):
        c = kaiten(c)
        heikoukaitenC.append(c)


def NotOK(p, q, r, i, j):
    cnt = (p[i][j] == "#") + (q[i][j] == "#") + (r[i][j] == "#")
    return (p[i][j] == "." and q[i][j] == "." and r[i][j] == ".") or cnt >= 2


for a in heikoukaitenA:
    for b in heikoukaitenB:
        for c in heikoukaitenC:
            flag = True
            for i in range(4):
                for j in range(4):
                    if NotOK(a, b, c, i, j):
                        flag = False
            if flag:
                print("Yes")
                exit()
print("No")
