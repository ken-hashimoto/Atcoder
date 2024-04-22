N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N - 1):
    a, na = A[i], A[i + 1]
    if a <= na:
        for j in range(a, na):
            ans.append(j)
    else:
        for j in range(a, na, -1):
            ans.append(j)

ans.append(A[-1])

print(*ans)
