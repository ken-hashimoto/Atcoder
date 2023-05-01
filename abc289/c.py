from itertools import product

N, M = map(int, input().split())
right = set(range(1, N + 1))
A_li = []
ans = 0
for i in range(M):
    C = int(input())
    A = set(map(int, input().split()))
    A_li.append(A)
# bit全探索
for bit in product((0, 1), repeat=M):
    tmp = set()
    for i in range(M):
        if bit[i] == 1:  # 下からi番目にbitが立っているとき
            tmp = tmp | A_li[i]
    if tmp == right:
        ans += 1

print(ans)
