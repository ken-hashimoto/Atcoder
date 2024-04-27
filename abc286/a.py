N, P, Q, R, S = map(int, input().split())
P -= 1
Q -= 1
R -= 1
S -= 1
A = list(map(int, input().split()))
B = []
for i in range(N):
    if P <= i <= Q:
        j = i - P
        B.append(A[R + j])
        continue
    if R <= i <= S:
        j = i - R
        B.append(A[P + j])
        continue
    else:
        B.append(A[i])
        continue
print(*B)
