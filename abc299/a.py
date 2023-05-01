N = int(input())
S = input()
isIn = False
for s in S:
    if s == "|":
        isIn = not isIn
    if s == "*":
        if isIn:
            print("in")
        else:
            print("out")
        exit()
