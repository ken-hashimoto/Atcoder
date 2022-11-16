N, x, y = map(int, input().split())
A = list(map(int, input().split()))
X = []
Y = []
normalize = 10**4
for i in range(N):
    if i % 2 == 0:
        X.append((A[i], i // 2))
    else:
        Y.append((A[i], (i - 1) // 2))
dp_x = [False for _ in range(2 * normalize + 10)]
dp_y = [False for _ in range(2 * normalize + 10)]
x += normalize
y += normalize
dp_x[0 + normalize] = True
dp_y[0 + normalize] = True
for i in range(len(X)):
    dp_new_x = [False for _ in range(2 * normalize + 10)]
    for j in range(len(dp_x)):
        if dp_x[j]:
            dp_new_x[j + X[i][0]] = True
            if i == 0:
                continue
            dp_new_x[j - X[i][0]] = True
    dp_x = dp_new_x
for i in range(len(Y)):
    dp_new_y = [False for _ in range(2 * normalize + 10)]
    for j in range(len(dp_y)):
        if dp_y[j]:
            dp_new_y[j + Y[i][0]] = True
            dp_new_y[j - Y[i][0]] = True
    dp_y = dp_new_y
if dp_x[x] and dp_y[y]:
    print("Yes")
else:
    print("No")
