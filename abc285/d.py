from collections import deque


N = int(input())
M = dict()
S_li = []
T_li = []
for i in range(N):
    S, T = input().split()
    M[S] = T
    S_li.append(S)
    T_li.append(T)
values = set(M.values())
d = deque()
for s in S_li:
    if s not in values:
        d.append(s)
tp_sorted = []
while d:
    v = d.popleft()
    tp_sorted.append(v)
    if v in M.keys():
        d.append(M[v])
inp = S_li + T_li
M = len(set(inp))
if len(tp_sorted) == M:
    print("Yes")
else:
    print("No")
