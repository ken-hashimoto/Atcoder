import math
A,B,K = map(int,input().split())
ans = 0
while B > A*K(**ans):
  ans += 1
print(ans)