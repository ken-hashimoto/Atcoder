def isAdj(a, b, m):
    return (a + 1) % m == b % m or a % m == b % m


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
S = sum(A)
double_A = A + A
ans = 0
tmp = 0
discard_cnt = 0
for i in range(2 * N):
    if discard_cnt == N:
        print(0)
        exit()
    if i == 0:
        tmp += double_A[i]
        discard_cnt += 1
        continue
    if isAdj(double_A[i - 1], double_A[i], M):
        tmp += double_A[i]
        discard_cnt += 1
    else:
        ans = max(ans, tmp)
        discard_cnt = 0
        tmp = double_A[i]
        discard_cnt += 1
print(S - ans)
