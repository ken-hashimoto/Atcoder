N = int(input())
S = input()
winner = ""
a = 0
t = 0
for i in range(N):
    if S[i] == "A":
        a += 1
        if a > t:
            winner = "A"
    if S[i] == "T":
        t += 1
        if a < t:
            winner = "T"
print(winner)