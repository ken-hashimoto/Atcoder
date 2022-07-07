N = int(input())
A = list(map(lambda x:int(x)%200,input().split()))
ans = 0
d = {i:0 for i in range(200)}
for a in A:
  d[a] += 1
for i in range(200):
  if d[i] >= 2:
    ans += d[i]*(d[i]-1)//2
print(ans)