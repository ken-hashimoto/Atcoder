from collections import deque


N,X = map(int,input().split())
S = input()
d = deque()
for s in S:
  if s == 'L' or s == 'R':
    d.append(s)
  if s == 'U':
    if d:
      v = d.pop()
      if v == 'R' or v == 'L': #LUかRUの並びは省略して良い
        continue
      else:
        d.append(v)
        d.append(s)
    else:
      d.append(s)
while d:
  v = d.popleft()
  if v == 'U':
    X = X//2
  if v == 'L':
    X = 2*X
  if v == 'R':
    X = 2*X + 1
print(X)