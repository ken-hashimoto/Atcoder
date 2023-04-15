A, B = map(int, input().split())
ans = 0
while True:
    if A < B:
        ans += B // A
        B = B % A
        if B == 0:
            ans -= 1
            break
    if A > B:
        ans += A // B
        A = A % B
        if A == 0:
            ans -= 1
            break
    if A == B:
        break
print(ans)
