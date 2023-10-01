N, M = map(int, input().split())
S = input()
T = input()

isPrefix = False
isSuffix = False
if T[:N] == S:
    isPrefix = True
if T[M - N :] == S:
    isSuffix = True

if isPrefix and isSuffix:
    print(0)
elif isPrefix and not isSuffix:
    print(1)
elif not isPrefix and isSuffix:
    print(2)
else:
    print(3)
