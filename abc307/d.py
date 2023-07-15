from collections import deque
N = int(input())
S = input()
d = deque()
bracket_cnt = 0
for s in S:
    if s == "(":
        bracket_cnt += 1
        d.append(s)
    elif s == ")":
        if bracket_cnt <= 0:
            d.append(s)
            continue
        while True:
            ss = d.pop()
            if ss == "(":
                break
        bracket_cnt -= 1
    else:
        d.append(s)
print("".join(d))

