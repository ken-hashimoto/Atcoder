N = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(N//7):
    tmp = 0
    for j in range(7):
        tmp += A[7*i + j]
    ans.append(tmp)
print(*ans)