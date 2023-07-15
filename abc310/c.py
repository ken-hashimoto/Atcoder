N = int(input())
s = set()
for i in range(N):
    S = input()
    revS = S[::-1]
    if revS < S:
        S = revS
    s.add(S)
print(len(s))
