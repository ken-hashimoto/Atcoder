N = int(input())
S = []
one = ["H", "D", "C", "S"]
second = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]


for i in range(N):
    s = input()
    S.append(s)
    if not s[0] in one or not s[1] in second:
        print("No")
        exit()
if len(S) == len(set(S)):
    print("Yes")
else:
    print("No")
