from collections import deque


S = input()
d = deque()
d.append((S,0))
seen = set()
seen.add(S)
while d:
  v = d.popleft()
  if v[0] == "atcoder":
    print(v[1])
    exit()
  for i in range(6):
    nv = list(v[0])
    nv[i],nv[i+1] = nv[i+1],nv[i]
    nv = "".join(nv)
    if nv in seen:
      continue
    seen.add(nv)
    d.append((nv,v[1]+1))
