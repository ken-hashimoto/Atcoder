R, C = map(int, input().split())
B = []
for r in range(R):
    b = list(input())
    B.append(b)
bombs = []
for i in range(R):
    for j in range(C):
        if B[i][j] != "." and B[i][j] != "#":
            bombs.append((B[i][j], (i, j)))


def d(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def is_destroyed(x, y):
    for bomb in bombs:
        if d(x, y, bomb[1][0], bomb[1][1]) <= int(bomb[0]):
            return True
    return False


for i in range(R):
    for j in range(C):
        if is_destroyed(i, j):
            B[i][j] = "."
for b in B:
    print("".join(b))
