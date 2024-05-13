import copy

S = list(input())
T = list(input())
if S == T:
    print("Yes")
    exit()
N = len(S)
for i in range(N - 1):
    temp_S = copy.copy(S)
    temp_T = copy.copy(T)
    temp_S[i], temp_S[i + 1] = temp_S[i + 1], temp_S[i]
    if temp_S == temp_T:
        print("Yes")
        exit()

print("No")
