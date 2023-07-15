N,P,Q = map(int,input().split())
D = list(map(int,input().split()))
ans = 10**18
for i in range(N):
    ans = min(D[i]+Q,ans)
ans = min(ans,P)
print(ans)