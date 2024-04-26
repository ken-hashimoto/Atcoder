N, Q = map(int, input().split())
p = [0 for _ in range(N)]
for i in range(Q):
    a, x = map(int, input().split())
    x -= 1
    if a == 1:
        p[x] += 1
    if a == 2:
        p[x] += 2
    if a == 3:
        if p[x] >= 2:
            print("Yes")
        else:
            print("No")
