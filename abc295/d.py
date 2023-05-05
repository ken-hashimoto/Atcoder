from itertools import product

S = list(input())
M = dict()
N = len(S)
ans = 0
for bit in product((0, 1), repeat=10):
    bit = map(str, bit)
    b = "".join(bit)
    M[b] = 0
M["0000000000"] = 1
now = ["0" for i in range(10)]
for i in range(N):
    s = S[i]
    int_s = int(s)
    if now[int_s - 1] == "0":
        now[int_s - 1] = "1"
    else:
        now[int_s - 1] = "0"
    k = "".join(now)
    ans += M[k]
    M[k] += 1
print(ans)
