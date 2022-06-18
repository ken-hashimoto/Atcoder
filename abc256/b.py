from copy import deepcopy


N = int(input())
A = list(map(int,input().split()))
G = [0]*4
nG = deepcopy(G)
ans = 0
for a in A:
  G[0] += 1
  nG[0] += 1
  for i in range(4):
    if G[i] > 0:
      nG[i] -= 1
      ni = i + a
      if ni > 3:
        ans += 1
      else:
        nG[ni] += 1
  G = deepcopy(nG)

print(ans)
