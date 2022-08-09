import itertools
N,M = map(int,input().split())
li = list(range(1,M+1))
for pair in itertools.combinations(li, N):
  pair = list(pair)
  pair.sort()
  print(*pair)
