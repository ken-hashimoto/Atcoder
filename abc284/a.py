N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)
S = S[::-1]
for s in S:
    print(s)
