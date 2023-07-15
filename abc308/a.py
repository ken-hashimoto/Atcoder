S = list(map(int,input().split()))
ss = sorted(S)
if S != ss:
    print("No")
    exit()
for s in S:
    if s%25 != 0:
        print("No")
        exit()
    if s < 100 or 675 < s:
        print("No")
        exit()
print("Yes")