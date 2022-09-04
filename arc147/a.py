from collections import deque


N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
d = deque(A)
ans = 0
while d:
  ans += 1
  M = d.popleft()
  if len(d) == 0:
    break
  m = d[-1]
  M = M%m
  if M == 0:
    continue
  d.append(M)

print(ans)