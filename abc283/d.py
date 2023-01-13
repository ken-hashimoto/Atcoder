from collections import deque

S = input()
alphabet = {chr(i): False for i in range(97, 97 + 27)}
d = deque()
N = len(S)
i = 0
for s in S:
    if s != "(" and s != ")":
        # sがalphabetであるとき
        if alphabet[s]:
            print("No")
            exit()
        alphabet[s] = True
        d.append(s)
        continue
    # sが()のいずれかであるとき
    if s == "(":
        d.append(s)
        continue
    if s == ")":
        while d:
            v = d.pop()
            if v == "(":
                break
            alphabet[v] = False
print("Yes")
