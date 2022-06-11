from collections import deque

Q = int(input())
d = deque()
for _ in range(Q):
  query = list(map(int,input().split()))
  num = query[0]
  if num == 1:
    x,c = query[1:]
    d.append((x,c))
  if num == 2:
    c = query[1]
    ans = 0
    while c > 0:
      x,cnt = d.popleft()
      ans += x*cnt
      c -= cnt
    if c < 0:
      d.appendleft((x,-c))
      ans -= x*(-c)
    print(ans)

