N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
winner = -1
max_cand = -1
for i in range(N):
    if C[i] == T:
        if R[i] > max_cand:
            winner = i + 1
            max_cand = R[i]
if winner != -1:
    print(winner)
    exit()
T = C[0]

max_cand = -1
for i in range(N):
    if C[i] == T:
        if R[i] > max_cand:
            winner = i + 1
            max_cand = R[i]
print(winner)
