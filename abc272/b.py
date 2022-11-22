N, M = map(int, input().split())
d = [set() for _ in range(N)]
for i in range(M):
    inp = list(map(int, input().split()))
    x = inp[1:]
    for xj in x:
        d[xj - 1].add(i + 1)
for i in range(N):
    for j in range(N):
        if len(d[i] & d[j]) == 0:
            print("No")
            exit()
print("Yes")
