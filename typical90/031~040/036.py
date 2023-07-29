# マンハッタン距離は(x,y) -> (x+y,x-y)の変換！！
# |X| = max(X,-X)の式変形


N, Q = map(int, input().split())
P = []
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    P.append((x + y, x - y))
    X.append((x + y))
    Y.append(x - y)

X_max = max(X)
Y_max = max(Y)
X_min = min(X)
Y_min = min(Y)
for i in range(Q):
    q = int(input())
    x, y = P[q - 1]
    print(max(X_max - x, x - X_min, Y_max - y, y - Y_min))
