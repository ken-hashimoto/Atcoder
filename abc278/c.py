N, Q = map(int, input().split())
Sets = dict()
for i in range(Q):
    t, a, b = map(int, input().split())
    if not a in Sets.keys():
        Sets[a] = set()
    if not b in Sets.keys():
        Sets[b] = set()
    if t == 1:
        Sets[a].add(b)
    if t == 2:
        Sets[a].discard(b)
    if t == 3:
        if b in Sets[a] and a in Sets[b]:
            print("Yes")
        else:
            print("No")
