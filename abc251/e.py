N = int(input())
A = [0] + list(map(int,input().split()))
INF = float('inf')
dp0 = [[INF]*2 for _ in range(N+10)]
dp0[1][0] = 0
for i in range(2,N+1):
  dp0[i][0] = dp0[i-1][1]
  dp0[i][1] = min(dp0[i-1][0],dp0[i-1][1]) + A[i]
dp1 = [[INF]*2 for _ in range(N+10)]
dp1[1][1] = A[1]
for i in range(2,N+1):
  dp1[i][0] = dp1[i-1][1]
  dp1[i][1] = min(dp1[i-1][0],dp1[i-1][1]) + A[i]
ans = min(dp0[N][1],min(dp1[N][0],dp1[N][1]))
print(ans)