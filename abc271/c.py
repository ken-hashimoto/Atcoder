N = int(input())
A = set(map(int, input().split()))

ok = 0
ng = N + 1
while ok + 1 != ng:
    m = (ok + ng) // 2
    # 少なくともm巻まで読むことができるか？
    c = len(set(range(1, m + 1)) & A)  # Aのうちm巻までの本の数
    if c + (N - c) // 2 >= m:
        ok = m
    else:
        ng = m
print(ok)
