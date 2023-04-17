N = int(input())
S = input()
prev = ""
for i in range(N - 1):
    if S[i] == S[i + 1]:
        print("No")
        exit()
print("Yes")
