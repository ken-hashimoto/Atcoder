import itertools

N,L,R = map(int,input().split())
A = list(map(int,input().split()))
Left = [0 for _ in range(N+1)]
Right = [0 for _ in range(N+1)]
#Left[i] = (A[0], ...,A[i-1]の数列に最適に操作を行ったときのA[0] + ... + A[i-1])
#Right[i] = (A[N-1], ...,A[N-i]の数列に最適に操作を行ったときのA[N-1]+ ... + A[N-i])
#求めるのはLeft[i] + Right[N-i]の最小値
for i in range(1,N+1):
  Left[i] = min(L*i,Left[i-1] + A[i-1])
for i in range(1,N+1):
  Right[i] = min(R*i,Right[i-1]+A[N-(i-1)-1])
ans = float('inf')
for i in range(N+1):
  ans = min(ans,Left[i] + Right[N-i])
print(ans)