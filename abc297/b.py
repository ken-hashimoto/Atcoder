S = input()
b = []
k = 0
r = []
for i in range(8):
    if S[i] == "B":
        b.append(i + 1)
    if S[i] == "K":
        k = i + 1
    if S[i] == "R":
        r.append(i + 1)
if (b[0] % 2 == 0 and b[1] % 2 == 1) or (b[1] % 2 == 0 and b[0] % 2 == 1):
    if r[0] < k < r[1]:
        print("Yes")
        exit()
print("No")
