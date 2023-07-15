def trim_grid(grid):
    min_i = min_j = float('inf')
    max_i = max_j = float('-inf')

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                min_i = min(min_i, i)
                max_i = max(max_i, i)
                min_j = min(min_j, j)
                max_j = max(max_j, j)
    trimmed_grid = [row[min_j:max_j+1] for row in grid[min_i:max_i+1]]

    return trimmed_grid

Ha,Wa = map(int,input().split())
Sa = []
for i in range(Ha):
    a = list(input())
    Sa.append(a)
Sa = trim_grid(Sa)
Ha = len(Sa)
Wa = len(Sa[0])
Sb = []
Hb,Wb = map(int,input().split())
for i in range(Hb):
    b = list(input())
    Sb.append(b)
Sb = trim_grid(Sb)
Hb = len(Sb)
Wb = len(Sb[0])
Hx,Wx = map(int,input().split())
Sx = []
for i in range(Hx):
    x = list(input())
    Sx.append(x)
Sx = trim_grid(Sx)
Hx = len(Sx)
Wx = len(Sx[0])
# Xを固定してAとBを動かす全探索

def harituke(i,j,S,H,W):
    global Hx,Wx
    C = [["."]* Wx for _ in range(Hx)]
    for k in range(H):
        for l in range(W):
            if 0 <= i+k < Hx and 0 <= j+l < Wx:
                C[i+k][j+l] = S[k][l]
            else:
                return -1
    return C
def merge(S1,S2):
    global Hx,Wx
    C = [["."]* Wx for _ in range(Hx)]
    for i in range(Hx):
        for j in range(Wx):
            if S1[i][j] == "#" or S2[i][j] == "#":
                C[i][j] = "#"
    return C
for ai in range(Hx):
    for aj in range(Wx):
        A_harituke = harituke(ai,aj,Sa,Ha,Wa)
        if A_harituke == -1:
            continue
        for bi in range(Hx):
            for bj in range(Wx):
                B_harituke = harituke(bi,bj,Sb,Hb,Wb)
                if B_harituke == -1:
                    continue
                expect = merge(A_harituke,B_harituke)
                if expect == Sx:
                    print("Yes")
                    exit()
print("No")