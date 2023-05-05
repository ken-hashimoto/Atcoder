from collections import deque

Q = int(input())
d = deque([1])
mod = 998244353
S = 1
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        S = 10 * S + query[1]
        d.append(query[1])
        S %= mod
    if query[0] == 2:
        p = d.popleft()
        S -= p * pow(10, len(d), mod)
        S %= mod
    if query[0] == 3:
        print(S % mod)
