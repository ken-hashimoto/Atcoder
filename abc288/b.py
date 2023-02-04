N, K = map(int, input().split())
names = []
for i in range(N):
    S = input()
    if i >= K:
        continue
    names.append(S)
names.sort()
for i in range(K):
    print(names[i])
