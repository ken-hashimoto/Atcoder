N = int(input())
S = list(input())

if S.count("x") == 0 and S.count("o") >= 1:
    print("Yes")
print("No")