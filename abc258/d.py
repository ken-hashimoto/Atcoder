N,X = map(int,input().split())
ans = float('inf')
before = 0
for i in range(N):
  if i == X:
    break 
  a,b = map(int,input().split())
  tmp = before + a + (X-i)*b
  ans = min(ans,tmp)
  before += a+b
print(ans)