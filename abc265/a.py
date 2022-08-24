X,Y,N = map(int,input().split())
ans = 10**9
for i in range(N+1):
  if (N-i)%3 == 0 and N - i >= 0:
    ans = min(ans,X*i + Y*((N-i)//3))
print(ans)