def isKaibun(s):
    return s == s[::-1]
N = int(input())
SS = []
for i in range(N):
    S = input()
    SS.append(S)
for i in range(N):
    for j in range(N):
        if i== j:
            continue
        if isKaibun(SS[i]+SS[j]):
            print("Yes")
            exit()
print("No")
