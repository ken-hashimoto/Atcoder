N = int(input())
A = list(map(int, input().split()))
ans = -1
m = max(A)
for a in A:
    if a == m:
        continue
    if a > ans:
        ans = a
print(ans)
