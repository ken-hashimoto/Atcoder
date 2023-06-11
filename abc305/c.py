H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]

def isBlank():
    if 0 <= i-1 < H  and 0 <= j+1 < W:
        if S[i-1][j] == "#" and S[i][j+1] == "#":
            return True
    if 0 <= i-1 < H and 0 <= j-1 < W:
        if S[i-1][j] == "#" and S[i][j-1] == "#":
            return True
    if 0 <= i+1 < H and  0 <= j+1 < W:
        if S[i+1][j] == "#" and S[i][j+1] == "#":
            return True
    if 0 <= i+1 < H and 0 <= j-1 < W:
        if S[i+1][j] == "#" and S[i][j-1] == "#":
            return True
    return False
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            if isBlank():
                print(i+1,j+1)
                exit()