N,M = map(int,input().split())
A_li = [0 for _ in range(M+1)]
B_li = [0 for _ in range(M+1)]
minB = 10**6

for _ in range(N):
  A,B = map(int,input().split())
  minB = min(minB,B)
  A_li[A] = max(A,A_li[A])
  B_li[A+1] = max(B_li[A+1],B)
for i in range(M-1,0,-1):
  A_li[i] = max(A_li[i+1],A_li[i])
for i in range(1,M+1):
  B_li[i] = max(B_li[i-1],B_li[i])
li = [0 for _ in range(minB+1)]
for i in range(1,minB+1):
  li[i] = max(A_li[i],B_li[i])
ans = [0 for _ in range(M+10)]
for ind in range(1,minB+1):
  cnt = li[ind]
  # (ind,...cnt) (長さcnt - ind + 1)
  # (ind,...cnt+1),...,
  # (ind,...,M) (長さM - ind + 1)
  ans[cnt-ind+1] += 1
  ans[M-ind+2] -= 1
for i in range(1,M+10):
  ans[i] += ans[i-1]
print(*ans[1:M+1])