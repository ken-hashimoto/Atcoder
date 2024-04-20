N = int(input())

p = [0 for _ in range(24)]
for i in range(N):
    w, x = map(int, input().split())
    for j in range(9):
        p[(x + j) % 24] += w
print(max(p))
