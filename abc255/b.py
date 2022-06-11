N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = []
zahyou = []
def dist(x,y,w,z):
  return (x-y)**2 + (w-z)**2
for _ in range(N):
  x,y = map(int,input().split())
  zahyou.append((x,y))

for i in range(N):
  m = 10**60
  for a in A:
    a -= 1
    x_i,y_i = zahyou[i]
    x_a,y_a = zahyou[a]
    m = min(m,dist(x_i,x_a,y_i,y_a))
  ans.append(m)
answer = max(ans)**0.5
print(answer)