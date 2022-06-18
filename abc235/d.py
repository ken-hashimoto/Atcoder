from collections import deque
import sys
sys.setrecursionlimit(10**7)
a,N = map(int,input().split())
M = 10**6 + 10
d = deque()
d.append(1)
ans = [-1]*M
ans[1] = 0
while d:
  v = d.popleft()
  op1 = a*v
  if op1 < M and ans[op1] == -1:
    ans[op1] = ans[v] + 1
    d.append(op1)
  if v >= 10 and v%10 != 0:
    sv = str(v)
    op2 = int(sv[-1] + sv[:-1])
    if op2 < M and ans[op2] == -1:
      ans[op2] = ans[v] + 1
      d.append(op2)
  

print(ans[N])